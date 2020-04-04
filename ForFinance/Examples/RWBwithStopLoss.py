#Richard Moglen Jan 2020 Backtest of RWB strategies
#import necessary packages/libraries
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import statistics
import time

yf.pdr_override() # Activate yahoo finance workaround
now = dt.datetime.now() #Runs until todays date
print()
stock = input("Enter the stock symbol (enter 'quit' to stop): ") #Query user for stock ticker

while stock != "quit": #Runs this loop until user enters 'quit' (can do many stocks in a row)
	startString= input("Enter Date to start Backtest (ex: 12/4/2003): ") #Query user 
	startList=list(map(int,(startString.split('/')))) #Split string into an array
	startyear=startList[2] #assign 3rd element in array to startyear
	startmonth=startList[0] #assign 1st element in array to startyear
	startday=startList[1] #assign 2nd element in array to startyear
	start =dt.datetime(startyear,startmonth,startday) #Set starting time for datasample
	startalt =dt.datetime(startyear-1,startmonth,startday) #Set starting time for datasample
	
	df = pdr.get_data_yahoo(stock, startalt, now) #create panda dataframe with stock data

	sEMAs = input("Enter 6 short term EMAs seperated by a ',' ") #Query user 
	sEMAsList=list(map(int, (sEMAs.split(',')))) #Split string into array full of short term ema values


	lEMAs = input("Enter 6 long term EMAs seperated by a ',' ") #Query user 
	lEMAsList=list(map(int, (lEMAs.split(',')))) #Split string into array full of longer term ema values
	emasUsed=sEMAsList #Add short term array to total emas array
	emasUsed.extend(lEMAsList) #add longer term ema array to overall emas array

	columnList=[] #Creates array that will store ema periods used
	for x in emasUsed: #This for loop calculates the EMAs for te stated periods and appends to dataframe
		ema=x
		columnList.append('EMA_'+str(ema)) #add ema to column array
		df['EMA_'+str(ema)] = round(df.iloc[:,4].ewm(span=ema,adjust=False).mean(),2) #calculate ema and append to pandas datafram as its own column

	sma=0 #Initialize sma period variable
	smaq=input("Enter Critical SMA (Enter 0 if you don't want to use one) ") #prompt user for simple moving average. Given a 200 day, the program will only enter if the price of the stock is above its 200 day

	if (smaq!="0"): #Check if given a sma greater than 0
		sma=int(smaq) #converts string to int
		df['SMA_'+str(sma)] = df.iloc[:,4].rolling(window=sma).mean() #calculates sma and creates a column in the dataframe
		checksma=True #This variable tells the program wether it has to check the sma restriction
	else:
		checksma=False # If no sma restiction,no need to check sma
		SMAchecked=True # If no sma restiction, set checked to true


	num=0
	delrow=0
	stop=0
	#This loop counts the rows from the start of the datafram up to the start date
	for i in df.index:
		if(i>start and stop==0):
			delrow=num
			stop=1
		else:
			num+=1

	df=df.iloc[max((delrow),sma):] #delete either the sma period or delrow from the dataframe, whichever is largest

	pos=0 #This variable identifies wether we would be in the stock or not. 1 if yes, 0 if no
	percentchange=[] #create list to store each trades results
	numDaysG=[] #create list to store days held for gains
	numDaysL=[] #create list to store days held for losses
	num=0 #counts for loop iterations
	maxloss=float(input("Enter Stop Loss %: (100 for none) ")) #Sets Max percentage loss
	hitstop=0 #This variable  keeps track of wether the stop loss was exceeded
	
	for i in df.index: #Iterate through all days to check RWB pattern
		cmin=min(df[columnList[0]][i], df[columnList[1]][i],df[columnList[2]][i], df[columnList[3]][i], df[columnList[4]][i], df[columnList[5]][i]) #calculates the minimum of the short term EMAs
		cmax=max(df[columnList[6]][i], df[columnList[7]][i],df[columnList[8]][i], df[columnList[9]][i], df[columnList[10]][i], df[columnList[11]][i]) #calculates the maximum of the longer term EMAs
		

		if(checksma==True): #runs if there is a sma restriction
			if(df['Adj Close'][i]>df['SMA_'+str(sma)][i]): #checks if current close> sma restriction
				SMAchecked=True 
			else:
				SMAchecked=False

		if(pos==1): #Do I already have a position
			cp=df['Adj Close'][i] #set current price
			pc=((cp/bp)-1)*100 #calculate percent change on position

			if(pc<(-maxloss) and hitstop!=1): #Should the stop loss be hit
				hitstop=1
				sp=cp #Set sell price
				#print("Stop hit, Current PC: "+str(pc)+" on "+str(i))
				edate=i

		if((cmin>cmax) and SMAchecked): #Is the min of the short term EMAs greater than the max longer term (Is RWB?)

			if(pos==0): #Checks if not in the stock if so will buy
				bp=df['Adj Close'][i] #Set buy price
				pos=1 #turn on pos to indicate that we are buying stock at this point
				print('Buying now at ' +str(bp)+ " on "+ str(i))
				sdate=i
				currentPC=0 


		elif(cmin<cmax): #If not in RWB pattern
			#print(str(i)+": Blue White Red, Close: "+str(df['Adj Close'][i]))
			if(pos==1): #Checks if we own the stock if so will sell 
				if (hitstop!=1):
					sp=df['Adj Close'][i] #set sell price
					edate=i
				pc=((sp/bp)-1)*100 #calculates the percentage change of the trade
				#print(str(pc))
				percentchange.append(pc) #adds this trade to list
				pos=0 #since we no longer own it, sets pos to off
				hitstop=0
				print('Selling now at ' +str(sp)+ " on "+ str(i)+' Percent Change: '+str(pc)+'%')
				
				daysheld=pd.date_range(sdate, edate, freq='B').size #Calculate days held

				if(pc>0): #Check if winning or losing trade, append days held value to relevant array
					numDaysG.append(daysheld)
				else:
					numDaysL.append(daysheld)
				#print("Number of days held: "+str(daysheld))

		if (num==(df['Adj Close'].count()-1) and pos==1): # checks if most current value (if yes maybe need to sell to get most current trade)
			sp=df['Adj Close'][i] #set sell price
			pc=((sp/bp)-1)*100 #calc percentage change
			print('Selling now at ' +str(sp)+ " on "+ str(i)+' Percent Change: '+str(pc)+'%') #print out sell message
			edate=i #set end date equal to the current date being considered
			daysheld=pd.date_range(sdate, edate, freq='B').size #Calculates number of days held
			#print("Number of days held: "+str(daysheld))
			percentchange.append(pc) #add to list 
			if(pc>0):
				numDaysG.append(daysheld)
			else:
				numDaysL.append(daysheld)
		num+=1 #add 1 to counter 

	#print("Trade Results: ", end =" ")
	#print(percentchange)
	#Now to analyze the results which are stored in list: percentchange
	gains=0 #will keep track of percentage gains
	ng=0 #will keep track of # of trades which were gains
	losses=0 #will keep track of percentage losses
	nl=0 #will keep track of # of trades which were losses
	totalR=1 #will keep track of total return with the strategy
	for i in percentchange: #This loop iterates through the list keeps track of core statistics
		if(i>0):
			gains+=i
			ng+=1
		else:
			losses+=i
			nl+=1
		totalR=totalR*((i/100)+1) #Calculates total Return
	totalR=round((totalR-1)*100,2)
	if(ng>0):
		avgGain=gains/ng #calculate the average gain from winning trades
		maxR=str(max(percentchange))
		avgDG=str(round(sum(numDaysG)/len(numDaysG),1))
	else:
		avgGain=0
		maxR='undefined'
		avgDG="undefined"
	if(nl>0):
		avgLoss=losses/nl #calculate the average loss from losing trades
		ratio=str(-avgGain/avgLoss)
		maxL=str(min(percentchange))
		avgDL=str(round(sum(numDaysL)/len(numDaysL),1))
	else:
		avgLoss=0
		maxL="undefined"
		ratio="inf"
		avgDL="undefined"
	if(ng>0 or nl >0):
		battingAvg=ng/(ng+nl) #calculate the percentage of trades which were gains
	else:
		battingAvg=0

	n=10 #Number of simulated trades
	nReturn=round(((((1+(avgGain/100))**(n*battingAvg))*((1+(avgLoss/100))**(n*battingAvg)))-1)*100,2) #this is long but all it does is simulates n trades and provides result

	#print out results
	#print(percentchange)
	print()
	print()
	print("Results for "+ stock +" going back to "+str(df.index[0])[:10]+", Sample size: "+str(ng+nl)+" trades")
	print("EMAs used: "+str(emasUsed))
	print("Stoploss: "+str(maxloss)+"%")
	print("Batting Avg: "+ str(battingAvg))
	print("Gain/loss ratio: "+ ratio)
	print("Average Gain: "+ str(avgGain))
	print("Average Loss: "+ str(avgLoss))
	print("Max Return: "+ maxR)
	print("Max Loss: "+ maxL)
	print("Average Days held for gains: "+ avgDG)
	print("Average Days held for Losses: "+ avgDL)
	print()
	print("Total return over "+str(ng+nl)+ " trades: "+ str(totalR)+"%" )
	print("Starting with $10000, this would turn into $"+str(round(10000*((totalR/100)+1),2)))
	print("Example return Simulating "+str(n)+ " trades: "+ str(nReturn)+"%" )

	print()
	stock = input("Enter the stock symbol (enter 'quit' to stop): ") #query user for next stock
	