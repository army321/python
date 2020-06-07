import numpy
import scipy.special
import matplotlib.pyplot as plt

class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inode = inputnodes
        self.hnode = hiddennodes
        self.onode = outputnodes

        self.lr = learningrate

        # 链接权重矩阵，WIH和who？
        # 在数组ara wij中的权重，其中链接来自节点
        # numpy.random.normal 正态分布采样
        self.wih = numpy.random.normal(
                    0.0,
                    pow(self.hnode, -0.5),  # pow() 函数 x 的 y 次幂 (xy) 的值
                    (self.hnode, self.inode)
                    )
        self.who = numpy.random.normal(
            0.0,
            pow(self.onode, -0.5),
            (self.onode, self.hnode)
            )
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # train the neural network  训练神经网络
    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T  # 矩阵转换
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)  # dot()函数是矩阵乘
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)
        self.who += self.lr * numpy.dot(
                    (output_errors * final_outputs * (1.0 - final_outputs)),
                    numpy.transpose(hidden_outputs)
                    )
        self.wih += self.lr * numpy.dot(
                    (hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                    numpy.transpose(inputs)
                    )
        pass

    # query the neural network 查询神经网络
    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        # calculate signals into hidden layer 计算信号进入隐藏层
        hidden_inputs = numpy.dot(self.wih, inputs)  # dot()函数是矩阵乘
        # 计算隐藏层的信号 calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # calculate signals into final output layer 计算信号进入最终输出层
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

if __name__ == "__main__":
    input_nodes = 784
    hidden_nodes = 100
    output_nodes = 10
    learning_rate = 0.3
    # 初始化神经网络
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    # 定义权重矩阵 感好高端的名字。。
   # array = numpy.random.rand(3, 3) - 0.5
    #print(array)
    training_data_file = open('test_img.csv', 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    data_file_result = open('test_labels.csv', 'r')
    data_list_result = data_file_result.readlines()
    data_file_result.close()
    # print('读取的内容是：' + data_list_result[0])


    for i in range(len(training_data_list)):
        all_values = training_data_list[i].split(',')
        inputs = (numpy.asfarray(all_values)/255.0 * 0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(data_list_result[i])] = 0.99
        n.train(inputs, targets)

# 测试数据
    print('over')
    test_data_file = open('train_img.csv', 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    for i in range(10):
        all_values = test_data_list[i].split(',')
        result = n.query((numpy.asfarray(all_values)/255.0*0.99)+0.01)
        result_num = numpy.argmax(result)
        # print('返回的：' + str(result))
        print('返回的结果是：' + str(result_num))
     #   image_array = numpy.asfarray(all_values).reshape((28, 28))
    # print(image_array)
     #   plt.imshow(image_array, cmap='Greys', interpolation='None')
     #   plt.show()

  #  result = n.query((numpy.asfarray(all_values)/255.0*0.99)+0.01)
  #  print(result)
