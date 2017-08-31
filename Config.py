#coding:utf-8

class Config(object):
    init_scale = 0.04 #参数是用均匀分布进行初始化，该值为均匀分布的上下界
    learning_rate = 0.001 #学习率
    max_grad_norm = 15 #对梯度进行规划化（gradient clipping）
    num_layers = 3 #RNN的层级数
    num_steps = 15 # RNN展开的步骤数（每次训练多少个字符）
    hidden_size = 800 # 神经网络隐含层的维度
    iteration = 100 #模型总共迭代次数
    save_freq = 10 #每迭代多少次保存一次模型，同时进行一次生成
    keep_prob = 0.5 #dropout的概率
    batch_size = 128 #min-batch的大小
    model_path = './model/Model' #模型保存的路径
    
    #parameters for generation
    save_time = 90 #载入第save_time次保存的模型
    is_sample = True #是否采用sample策略，设置为False是采用max策略
    is_beams = True #是否采用beam-search进行解码，设置为False时不采用（相当于beam_size=1）
    beam_size = 2 #beam-search的窗口大小
    len_of_generation = 3500 #期望生成文本的长度（包括多少个字）
    gen_path = './output/output.txt' #生成文本的保存路径
    start_sentence = u'他回头看' #期望生成文本的开始部分（可以是一个句子，一个词，也可以仅仅只是一个字）
