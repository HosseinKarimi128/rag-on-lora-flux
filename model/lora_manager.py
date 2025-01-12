def load_lora_weights(pipe, lora_info):
    """
    Given the pipeline object and a list of (lora_path, adapter_name) tuples,
    load each LoRA into the pipeline.
    """
    for lora_path, adapter_name in lora_info:
        pipe.load_lora_weights(lora_path, adapter_name=adapter_name)
    return pipe

def unload_lora_weights(pipe):
    """
    Given the pipeline object, unload each LoRA from the pipeline.
    """
            
    return pipe.unload_lora_weights(lora_path, adapter_name=adapter_name)

def set_lora_weights(pipe, adapter_names, adapter_weights):
    """
    Given a list of adapter names and corresponding adapter weights,
    apply them to the pipeline.
    """
    pipe.set_adapters(adapter_names, adapter_weights=adapter_weights)
    return pipe
