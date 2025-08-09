# There are two types of xpath
# 1.Absolute Xpath: Absolute xpath follows the entire path of DOM structure to locate
#                   any element.
#    e.g /html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input
#    #Note : absolute xpath is not recommended to user, because it is very unstable
# 2.Relative Xpath: Relative Xpath find the element with the help of element attribute:
#      e.g.  //tagname[@attribute = 'value'] or //*[@attribute='value']
#      --> //input[@type = 'text'] or //*[@type=text]
#
# what if two elements have same attribute:
# say there are 2 elements with type = hidden - go for indexing
# (//input[@type='hidden'])[1]
#
# Methods of Xpath
#
# a) text()  - We can find an element with the text of an element visible.
                   e.g //tagname[text() = 'text_value'] or //*[text().'text value']
                    -->  //a[text()='Create new account'] or
                    -->//button[text()=' Log in']
