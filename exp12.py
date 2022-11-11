import pandas as pd
import matplotlib.pyplot as plt

author=['A','B','C']
article=[1,2,3]
auth_series=pd.Series(author)
article_series=pd.Series(article)
print(article_series)
print(type(auth_series))
frame={"Author":auth_series,"Article":article_series}
#print(type(frame))
result=pd.DataFrame(frame)
print(type(result))
age=[19,20,21]
result["age"]=pd.Series(age)
print(result)
result.plot.bar()
plt.show()