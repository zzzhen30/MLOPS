import os
import mlflow
import argparse # get the import from user
import time

def eval(p1,p2): 
    output_metric = p1**2 + p2**2
    return output_metric

# below function access two important input
def main(inp1,inp2):
    mlflow.set_experiment("Demo_Experiment")
    
    with mlflow.start_run(): # if not assign a run_name like below, it will create a unique run name
    #with mlflow.start_run(run_name='Example Demo'):
        mlflow.set_tag("version","1.0.0") # same as day2_help.py
        mlflow.log_param("param1",inp1) # log whatever the input is as parameter
        mlflow.log_param("param2",inp2) # key, value
        metric = eval(p1=inp1,p2=inp2)
        mlflow.log_metric("Eval_Metric",metric)
        os.makedirs("dummy",exist_ok=True)
        with open("dummy/example.txt","wt") as f:
            f.write(f"Artifactg created at {time.asctime()}")
        mlflow.log_artifact("dummy")


# get the cmd line argument, when getting the request to running the script
if __name__ == '__main__': 
    args = argparse.ArgumentParser() # read input from the user, argument parse method. after adding this obj,we can add argument
    args.add_argument("--param1","-p1",type=int,default=5)
    args.add_argument("--param2","-p2",type=int,default=10)
    
    parsed_args= args.parse_args() 
    # parsed_args.param1   # we can access the parameter
    main(parsed_args.param1 , parsed_args.param2)  # so it will be sent through the cmd to the main function 