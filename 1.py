# Import Parsl
import parsl
from parsl import *



# Let's create a pool of threads to execute our functions''''''''''''''''''''''''''''
workers = ThreadPoolExecutor(max_workers=4)
# We pass the workers to the DataFlowKernel which will execute our Apps over the workers.
dfk = DataFlowKernel(workers)



"""# Here we define our first App function, a simple python app that returns a string
@App('python', dfk)
def hello ():
    return 'Hello World!'

app_future = hello()



# Check status
print("Status: ", app_future.done())

# Get result
print("Result: ", app_future.result())"""

"""

@App('python', dfk)
def pi(total):
    import random      # App functions have to import modules they will use.
    width = 10000      # Set the size of the box in which we drop random points
    center = width/2
    c2  = center**2
    count = 0
    for i in range(total):
        # Drop a random point in the box.
        x,y = random.randint(1, width),random.randint(1, width)
        # Count points within the circle
        if (x-center)**2 + (y-center)**2 < c2:
            count += 1
    return (count*4/total)

@App('python', dfk)
def mysum(a,b,c):
    return (a+b+c)/3



a, b, c = pi(10**6), pi(10**6), pi(10**6)
avg_pi  = mysum(a, b, c)

print(avg_pi.done())

# Print the results
print("A: {0:5} B: {1:5} B: {2:5}".format(a.result(), b.result(), c.result()))##########
print("Average: {0:5}".format(avg_pi.result()))

print(avg_pi.done())"""





#################################################

@App('bash', dfk)
def sim_mol_dyn(i, dur, outputs=[], stdout=None, stderr=None):
    # The bash app function, requires that the bash script is assigned to the special variable
    # cmd_line. Positional and Keyword args to the fn() are formatted into the cmd_line string
    cmd_line = '''echo "{0}" > {outputs[0]}
    sleep {1};
    ls ;
    '''
# We call sim_mol_dyn with
sim_fut, data_futs = sim_mol_dyn(5, 3, outputs=['sim.out'], stdout='stdout.txt', stderr='stderr.txt')

print(sim_fut, data_futs)
