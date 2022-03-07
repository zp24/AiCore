
def with_job_title(func): #decorator
    def wrapper(start_date, finish_date): #wrapper
        a = "Lawyer"
        #print(a)
        func(a, start_date, finish_date)
        
    return wrapper
    
def employment(job_title, start_date, finish_date): #parameters
    
    #print("Paralegal", "February 2021", "January 2022")
    
    employment_list = [job_title, start_date, finish_date]

    #assign elements of a list to multiple variables
    #job_title, start_date, finish_date = employment_list
    #assigns first, second and third elements of employment_list to job_title, start_date and finish_date variables

    #job_title, start_date, *other = employment_list
    employment_list_dic = {job_title: " ", start_date: " ", finish_date: " "}
    #print(type(employment_list_dic))

    #for info in employment_list_dic: #show dictionary entries
     #       print("dictionary entries: ", info)
    
    job_title, start_date, finish_date = employment_list
    print(job_title)
    #print(job_title)
    print(start_date)
    #print(other) #prints out in ['']
    print(finish_date)
    #employment(*employment_list_dic)
    #try:
     #   employment(*employment_list)
    #except RecursionError:
     #   "Keeps unpacking"
#y = employment(*[None, "February 2021", "January 2022"]) #arguments *[] passes 3 arguments
y = employment(**{"job_title": "Paralegal", "start_date": "February 2021", "finish_date": "January 2022"}) #keyword argument
x = with_job_title(employment) 

x("February 1999", "February 2022")
x(**{"start_date": "February 2021", "finish_date": "January 2022"})