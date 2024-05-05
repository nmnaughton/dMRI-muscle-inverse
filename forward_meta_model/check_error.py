def check_error(args):
    # global meta_model
    inputs, order, val, DTI_indices, DTI_range = args
    mod = meta_model_local[order][val]
    eval_temp = mod(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6])
    err = (eval_temp - DTI_indices)/(DTI_range)*100
    return (err) 

# make the meta model in the processes global memory so it doesn't need to be sent each time (Which is very slow)
def init_worker(meta_model):
    global meta_model_local
    meta_model_local = meta_model
