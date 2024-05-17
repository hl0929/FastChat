export LOGDIR="logs"
export CUDA_VISIBLE_DEVICES=7
python3 -m fastchat.serve.model_worker \
    --model-path /root/models/Meta-Llama-3-8B-Instruct \
    --controller-address http://0.0.0.0:21001 \
    --host 0.0.0.0 \
    --port 21002 \
    --worker-address http://0.0.0.0:21002 
