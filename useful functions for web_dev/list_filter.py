# two ideas for filtering a given list, in this example the results of a test at school

test_results = [66.00, 75.00, 30.00, 81.00, 12.00, 25.00, 94.00, 90.00, 87.00, 0.00,
                16.00, 78.00, 99.00, 92.00, 76.00, 14.00, 0.00, 49.5, 94.00, 97.00]
# students only pass with 50/100 points or more, an unlucky one failed with 49.5

# first idea with lambda function:
passed_students1 = list(filter(lambda x: x >= 50, test_results))
print(passed_students1)

# second idea, using list comprehension:
passed_students2 = [i if i >=50 else "not passed" for i in test_results]
print(passed_students2)