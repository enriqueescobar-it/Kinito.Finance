
## Calculating & Comparing risk

### Calculating Return

#### Annual

Annual Return = ((Daily Return + 1)^365)*100-1

#### Single Equity

Logarithmic Rate of Return
![CalculatingAndComparingRisk-LogRateReturn](img/CalculatingAndComparingRisk-LogRateReturn.png "CalculatingAndComparingRisk-LogRateReturn")

$$
ln( \frac{P_t}{P_{t-1}} )
$$

#### Multiple Equities

Simple Rate of Return
![CalculatingAndComparingRisk-SimpleRateReturn](img/CalculatingAndComparingRisk-SimpleRateReturn.png "CalculatingAndComparingRisk-SimpleRateReturn")

$$
\frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
$$

##### Normalization to 100 to visualize

$$
\frac{P_1} {P_0} * 100
$$

##### Dot Product from Average Retrurn by Weights

![CalculatingAndComparingRisk-DotProduct](img/CalculatingAndComparingRisk-DotProduct.png "CalculatingAndComparingRisk-DotProduct")

Run permutation calculations

#### Popular Market Indices

S&P500: '^GSPC' 500 largest US companies reflects its diversity

DowJones: '^DJI' Industrial Average 30 largest

NASDAQ: '^IXIC' Composite Grouped Securities & IT Companies

FTSE100: '^FTSE' UK

DAX30: '^GDAXI' GER

NIKKEI225: JPN

MSCI: Morgan Stanley Composite International

### Calculating Rate of Return RoR

![CalculatingAndComparingRisk-RateOfReturn](img/CalculatingAndComparingRisk-RateOfReturn.png "CalculatingAndComparingRisk-RateOfReturn")

## Measuring Investment Risk

### Variance & Standard Deviation

![MeasuringInvestmentRisk-VARandSTD](img/MeasuringInvestmentRisk-VARandSTD.png "MeasuringInvestmentRisk-VARandSTD")

### Coviariance between 2 values

![MeasuringInvestmentRisk-Covariance](img/MeasuringInvestmentRisk-Covariance.png "MeasuringInvestmentRisk-Covariance")

* cov > 0 : both move in the same direction
* cov = 0 : both are independent
* cov < 0 : both move in opposite direction

### Correlation between 2 values

![MeasuringInvestmentRisk-CovarianceCorrelation](img/MeasuringInvestmentRisk-CovarianceCorrelation.png "MeasuringInvestmentRisk-CovarianceCorrelation")

* Corr(returns) : Dependence between prices at different times, focus on returns of your portfolio.
* Corr(prices) : focus on price levels
* variance = Dot Product (weights as Vector, Dot Product (252*cov(returns), weights) )
* volatility = sqrt(Dot Product (weights as Vector, Dot Product (252*cov(returns), weights) ))

## Regressions for Financial Analysis

* univariate regression: one variable (line = intercept + slope * x + residuals)
* multivariate regression: multiple variables

### Good regression

![MeasuringInvestmentRisk-TSS](img/MeasuringInvestmentRisk-TSS.png "MeasuringInvestmentRisk-TSS")

Higher percent implies more predictive is: R square = 1 - (SSR / TSS)

## Markowitz Portfolio Optimization

Distribute to have low correlation

Perform many iterations for performance graph
![MeasuringInvestmentRisk-EfficientFrontier](img/MeasuringInvestmentRisk-EfficientFrontier.png "MeasuringInvestmentRisk-EfficientFrontier")

## Capital Asset Pricing Model

Capital Market Line
![CapitalAssetPricingModel-CapitalMarketLine](img/CapitalAssetPricingModel-CapitalMarketLine.png "CapitalAssetPricingModel-CapitalMarketLine")

**Beta**
$$ 
\beta_{stock,market} = \frac{\sigma_{stock,market}}{\sigma_{market}^2}
$$

Beta = cov(stock, market) / variance of the market
Risk that cannot be avoided using diversification

* beta > 1 aggressive - performance follows the market
* beta = 0 no relationship
* beta < 1 defensive - performance follows slowly

![CapitalAssetPricingModel-CapitalMarketLineFormula](img/CapitalAssetPricingModel-CapitalMarketLineFormula.png "CapitalAssetPricingModel-CapitalMarketLineFormula")

**CAPM**
$$
 \overline{r_{stock}} = r_{free} + \beta_{stock,market}(\overline{r_{market}} - r_{free})
$$

**Equity Risk Premium**
$$(\overline{r_{market}} - r_{free})$$

Example for a US stock
* risk free: 2.5% (10 year US government bond yield)
* beta: 0.62 (S&P500 approximation) aka average premium
* equity risk premium: [4.5%, 5.5%] (historical in US)
* r(stock) = 2.5% + 0.62 * 5% = 5.6%

Sharpe Ratio allows to compare 2 stocks or 2 portfolios

![CapitalAssetPricingModel-SharpeRatio](img/CapitalAssetPricingModel-SharpeRatio.png "CapitalAssetPricingModel-SharpeRatio")

**Sharpe ratio:**
$$
Sharpe = \frac{\overline{r_{stock}} - r_{free}}{\sigma_{stock}}
$$

CAPM alpha

![CapitalAssetPricingModel-CAPMalpha](img/CapitalAssetPricingModel-CAPMalpha.png "CapitalAssetPricingModel-CAPMalpha")

## Multivariate Regression Analysis

Univariate regression has a unique beta coefficient and unique explanatory variable

![MultivariateRegressionAnalysis-Univariate](img/MultivariateRegressionAnalysis-Univariate.png "MultivariateRegressionAnalysis-Univariate")

Multivariate regression has a multiple beta coefficients and multiple explanatory variables

![MultivariateRegressionAnalysis-Multivariate](img/MultivariateRegressionAnalysis-Multivariate.png "MultivariateRegressionAnalysis-Multivariate")

## Monte Carlo Simulations for Decision Making Tool

### Using historical data

On revenues
* cogs: Gross Profits - cost of goods sold
* opex: Operating Profits

![MonteCarloSimulationAnalysis-Cogs](img/MonteCarloSimulationAnalysis-Cogs.png "MonteCarloSimulationAnalysis-Cogs")

![MonteCarloSimulationAnalysis-CogsNormal](img/MonteCarloSimulationAnalysis-CogsNormal.png "MonteCarloSimulationAnalysis-CogsNormal")

![MonteCarloSimulationAnalysis-Opex](img/MonteCarloSimulationAnalysis-Opex.png "MonteCarloSimulationAnalysis-Opex")

![MonteCarloSimulationAnalysis-OpexBinsAuto](img/MonteCarloSimulationAnalysis-OpexBinsAuto.png "MonteCarloSimulationAnalysis-OpexBinsAuto")

### Price Evolution

![MonteCarloSimulationAnalysis-PriceEvolution](img/MonteCarloSimulationAnalysis-PriceEvolution.png "MonteCarloSimulationAnalysis-PriceEvolution")

### Brownian Motion

#### Drift aka Expected Daily Return

$$
Drift = \mu - \frac{1}{2} \cdot var = \mu - \frac{1}{2} \cdot \sigma^2
$$

Direction headed in the past (calculate average, standard deviation, and variance f daily returns) in the historical period.

#### Volatility aka Random Variable

$$Random Variable = \sigma \cdot Z(Random(0,1))$$

* sigma is the historical variability
* Zeta is the number of standard deviation from mean

![MonteCarloSimulationAnalysis-PriceEvolutionFormula](img/MonteCarloSimulationAnalysis-PriceEvolutionFormula.png "MonteCarloSimulationAnalysis-PriceEvolutionFormula")

$$
\frac{P_t - P_{t-2}}{P_{t-2}}
$$

$$
ln(\frac{P_t}{P_{t-1}} ) = ln( \frac{P_t - P_{t-1}}{P_{t-1}} + \frac{P_{t-1}}{P_{t-1}}) = ln(\ simple.returns + 1)
$$


$$
daily\_returns = exp({drift} + {stdev} * z)
$$ 

$$
where\  z = norm.ppf(np.random.rand(t\_intervals, iterations))
$$

1. Historical Data

![MonteCarloSimulationAnalysis-Historical](img/MonteCarloSimulationAnalysis-Historical.png "MonteCarloSimulationAnalysis-Historical")

2. Log Returns: LogReturns = log(1 + returns_pct_change)

![MonteCarloSimulationAnalysis-LogReturns](img/MonteCarloSimulationAnalysis-LogReturns.png "MonteCarloSimulationAnalysis-LogReturns")

3. Mean Calculation : Mean = mean(LogReturns)
4. Variance Calculation : Variance = variance(LogReturns)
5. Drift Calculation : Drift = Mean - (Variance / 2)
6. Standard Deviation Calculation : Std = std(LogReturns)
7. Drift into Array Conversion
8. Set normalization at 95% norm.ppf(0.95)
9. Set array 10x2 of random values
8. Z Calculation : Z = norm.ppf(randomArray)
9. Set intervals & interations (1000,10)
10. r calculation : r = Drift + Std * Z
11. Daily Returns Calculation : DailyReturns = e^r
12. Price List Calculation : iterate to create matrix (first row has latest price value) m[t] = m[t-1] * DailyReturns[t]

![MonteCarloSimulationAnalysis-Formulas](img/MonteCarloSimulationAnalysis-Formulas.png "MonteCarloSimulationAnalysis-Formulas")

r = drift + stdev * Z
Z = norm.ppf(np.random.rand(t_intervals, iterations)
dailyReturns = exp(r) = exp(drift + stdev * Z) = exp(drift + stdev * norm.ppf(np.random.rand(tIntervals, iterations))

![MonteCarloSimulationAnalysis-Iteration](img/MonteCarloSimulationAnalysis-Iteration.png "MonteCarloSimulationAnalysis-Iteration")

###  Derivative Contracts

1. Forwards: price preset, one sells in N time to another
2. Futures: highly standardized foward contract on market place
3. Swaps: echange cashflows in N times of an asset (interest rate, stock price, bond price, commodity)
4. Options: owner buys (call options) or sells (put options) asset at a given price (strike price)

#### Derivative Pricing aka Black-Sholes-Merton

![MonteCarloSimulationAnalysis-Derivative-BlackSholes](img/MonteCarloSimulationAnalysis-Derivative-BlackSholes.png "MonteCarloSimulationAnalysis-Derivative-BlackSholes")

1. d1 : how much can we expect
2. d2 : how much we must pay


