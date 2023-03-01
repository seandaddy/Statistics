import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# pandas 패키지의 read_csv()를 이용해 cars.csv를 읽어 df라는 data.frame으로 저장합니다.
df=pd.read_csv('~/Documents/R script/data/cars.csv')
# statsmodels.api패키지의 OLS()함수로 y-절편없는 회귀분석을 합니다. 
model=sm.OLS(np.sqrt(df['dist']),df['speed']).fit()

# statsmodels.formula.api로 R같이 수식을 쓸 수 있습니다.
model2=smf.ols('np.sqrt(dist)~speed-1',data=df).fit()
print(model.summary(), model2.summary())
