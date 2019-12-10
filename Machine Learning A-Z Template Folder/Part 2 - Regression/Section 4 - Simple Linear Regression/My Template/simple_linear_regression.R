# Simple Linear Regression

# Importing the dataset
dataset = read.csv('Salary_Data.csv')
# dataset = dataset[, 2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)   #Random state
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# Fitting Simple Linear Regression to the Training set
# Salary is dependent value, YearsExperience is independent value

# Predicting the test set results
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)
y_pred = predict(regressor, newdata = test_set)

# Visualising the Training set results
# install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), 
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)), 
            colour = 'blue') +
  ggtitle ('Salary VS Experience (Training set)') + 
  xlab('Years of experience') +
  ylab('Salary')