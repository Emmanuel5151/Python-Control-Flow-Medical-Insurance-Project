#!/usr/bin/env python
# coding: utf-8

# # Python Control Flow: Medical Insurance Project

# In this project, you will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.
# 
# You will apply your knowledge of Python control flow to write code that gives people advice on how to lower their medical insurance costs.
# 
# Let's get started!

# ## Intro to Control Flow

# 1. First, take a look at the code in the code block below.
# 
#    The function `estimate_insurance_cost()` estimates the medical insurance cost for an individual, based on five variables:
#    - `age`: age of the individual in years
#    - `sex`: 0 for female, 1 if male
#    - `bmi`: individual's body mass index
#    - `num_of_children`: number of children the individual has
#    - `smoker`: 0 for a non-smoker, 1 for a smoker
#    
#    These variables are used in the following formula to estimate an individual's insurance cost:
#    
#    $$
#    insurance\_cost = 250*age - 128*sex + 370*bmi + 425*num\_of\_children + 24000*smoker - 12500
#    $$
#    
#    Take a look below the code at the estimated insurance cost for Keanu, a 29-year-old male smoker with three children and a BMI of 26.2.

# In[1]:


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)


# 2. Currently, our function prints out the estimated insurance cost based on values passed into the function. But it doesn't do much beyond that.
# 
#    It would be much more helpful if our function could provide more insight into how we can lower our insurance cost. We'll learn to do exactly that by using control flow - `if`, `elif`, and `else` statements - in our code.
#    
#    When you're ready, move on to the next step.

# In[ ]:





# ## Analyzing Smoker Status

# 3. In general, insurance costs are higher for smokers as well as people with a higher BMI. We can use the data from the variables `smoker` and `bmi` to provide advice on how to lower insurance costs.
# 
#    We'll first create a function that analyzes an individual's smoking status.
#    
#    In the code block below, define a function called `analyze_smoker()` that takes an input `smoker_status`. For now, the function should print `smoker_status`.

# In[1]:


def analyze_smoker(smoker_status):
  print(smoker_status)


# 4. Inside of the `analyze_smoker()` function, replace the print statement you wrote in the previous step with an `if/else` statement that does the following:
#    - If `smoker_status` is equal to `1`, print `"To lower your cost, you should consider quitting smoking."`
#    - Otherwise, print `"Smoking is not an issue for you."`

# In[2]:


def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")


# 5. Now that we've written the `analyze_smoker()` function, let's make use of it.
#  
#    In the `estimate_insurance_cost()` function, go to the line of code that prints the estimated insurance cost. On the next line, make a function call to `analyze_smoker()`, passing in the `smoker` variable as an argument.
#    
#    Run the code to see the result.

# In[4]:


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    # make function call to `analyze_smoker()` here
    analyze_smoker(smoker)
    return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)


# ## Analyzing BMI

# 6. Great job - you've created a simple function that notifies an individual if their insurance cost can be lowered by altering their smoking habits.
# 
#    Next, create a function that analyzes an individual's BMI (body mass index).
#    
#    Define a function below called `analyze_bmi()` that takes an input `bmi_value`. For now, the function should print `bmi_value`.

# In[5]:


def analyze_bmi(bmi_value):
  print(bmi_value)


# 7. Inside of this function we'll want to notify an individual whether their BMI can be improved, printing a personalized message based on the `bmi_value` passed in.
# 
#    According to the WHO (World Health Organization), here are the nutritional statuses for various BMI ranges:
#    - `BMI > 30:` obese
#    - `BMI >= 25 and BMI <= 30:` overweight
#    - `BMI >= 18.5 and BMI < 25:` normal weight
#    - `BMI < 18.5:` underweight
#    
#    Remove the print statement from the previous step and write code using `if`, `elif`, and `else` statements representing each of the following cases:
#    - `bmi_value > 30`: "Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI."
#    - `bmi_value >= 25 and bmi_value <= 30`: "Your BMI is in the overweight range. To lower your cost, you should lower your BMI."
#    - `bmi_value >= 18.5 and bmi_value < 25`: "Your BMI is in a healthy range."
#    - `bmi_value < 18.5`: "Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health."

# In[6]:


def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")


# 8. We now have a function that provides an individual guidance on how to lower their insurance cost by adjusting their BMI. Let's test this out!
# 
#    In the `estimate_insurance_cost()` function, under the line of code that calls the `analyze_smoker()` function, make a function call to `analyze_bmi()`, passing in the `bmi` variable as an argument.
#    
#    Run the code to see the result.
#    
#    Notice that now Keanu gets much more insight into actions he can take to lower his insurance cost. Keanu should consider quitting smoking and lowering his BMI if he wants to lower his medical insurance costs.

# In[3]:


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    # make function call to `analyze_smoker()` here
    analyze_smoker(smoker)
    # make function call to `analyze_bmi()` here
    
    return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)


# ## Analyze your own insurance cost

# 9. Now that we've estimated and analyzed Keanu's insurance cost, let's see if we can do the same for our own!
# 
#    In the code block below, create a new insurance cost variable for yourself, similar to how we did it for Keanu.
#    
#    Set the variable equal to a function call to `estimate_insurance_cost()`, passing in your own age, sex, BMI, number of children, and smoker status.
#    
#    Run the code to see the result. Do you see any ways that you can potentially lower your insurance cost?

# In[ ]:





# ## Extra

# 10. Great job! In this project, you used control flow in your code - using `if`, `elif`, and `else` statements - to provide advice on how individuals can lower their medical insurance costs.
# 
#     As a data scientist, it's important to have an understanding of control flow as you'll eventually work with and build complex decision tree algorithms. You are now better equipped to move forward in your data science journey!
#     
#     If you'd like additional practice on control flow, here are some ways you might extend this project:
#     - Use `try` and `except` statements to build error control into your code.
#     - In your `analyze_bmi()` function, notify the individual how much they need to lower their BMI to bring it to a normal weight range.
#     - Create a new function or code block that utilizes control flow in some way - feel free to experiment!
#     
#     Happy coding!

# In[ ]:





# In[ ]:




