# train
epoch = 200
num_classes = 41
batch_size = 16
device = 'cuda:0'  # cpu or 'cuda:0'
train_image_path = './disease/resnet_data/train/'  # 每个类别一个文件夹, 类别使用数字
valid_image_path = './disease/resnet_data/val/'  # 每个类别一个文件夹, 类别使用数字
num_workers = 4  # 加载数据集线程并发数
best_loss = 0.1  # 当loss小于等于该值会保存模型
save_model_iter = 20  # 每多少次保存一份模型
model_output_dir = './dis/resnet_cls/'
resume = False  # 是否从断点处开始训练
chkpt = './dis/resnet_cls/best_11.pth'  # 断点训练的模型
lr = 0.01

# predict
predict_model = './dis/resnet_cls/best_4.pth'
predict_image_path = './dis/numbers/test'  # 每个类别一个文件夹, 类别使用数字


image_format = 'png'
