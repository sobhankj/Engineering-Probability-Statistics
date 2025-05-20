import numpy as np, random
from keras.datasets import mnist
import tensorflow as tf
import matplotlib.pyplot as plt
from scipy import stats

def set_seed(seed):
    np.random.seed(seed)
    random.seed(seed)
    
set_seed(810109203)

(_ , _) , (test_images , _) = mnist.load_data()
test_images = test_images.reshape(test_images.shape[0] , -1)
test_images = test_images.astype('float32') / 255.0

autoencoder = tf.keras.models.load_model('mnist_AE.h5')
reconstructed_images = autoencoder.predict(test_images)

### albate choon ke seed moshakhas hast har dafee yek chiz ro neshon mide
# random_image = [0,0,0,0]
# for i in range(4) :
#   random_image[i] = np.random.randint(0, len(reconstructed_images))
    
im1_re = reconstructed_images[10]
im2_re = reconstructed_images[20]
im3_re = reconstructed_images[30]
im4_re = reconstructed_images[40]
im1 = test_images[10]
im2 = test_images[20]
im3 = test_images[30]
im4 = test_images[40]
image1_re = np.reshape(im1_re, (28,28))
image2_re = np.reshape(im2_re, (28,28))
image3_re = np.reshape(im3_re, (28,28))
image4_re = np.reshape(im4_re, (28,28))
image1 = np.reshape(im1, (28,28))
image2 = np.reshape(im2, (28,28))
image3 = np.reshape(im3, (28,28))
image4 = np.reshape(im4, (28,28))

# plt.subplot(1, 2, 1)  
# plt.imshow(image1)
# plt.subplot(1, 2, 2)
# plt.imshow(image1_re)

# plt.subplot(1, 2, 1)
# plt.imshow(image2)
# plt.subplot(1, 2, 2)
# plt.imshow(image2_re)

# plt.subplot(1, 2, 1)  
# plt.imshow(image3)
# plt.subplot(1, 2, 2)
# plt.imshow(image3_re)

# plt.subplot(1, 2, 1)  
# plt.imshow(image4)
# plt.subplot(1, 2, 2)
# plt.imshow(image4_re)

def MSE(x, y):
    mse = [0] * len(x)
    for i in range(len(x)) :
        for j in range(len(x[i])) :
            msei = (x[i][j] - y[i][j]) ** 2
            mse[i] = mse[i] + msei
        mse[i] = mse[i] / len(x[i])
    return mse
            
list_mse = MSE(test_images , reconstructed_images)

plot_mse = plt.hist(list_mse, bins=100)

mean_mse = np.mean(list_mse)
enheraf_mse = np.std(list_mse)

print(mean_mse , enheraf_mse)

ks_statistic, p_value = stats.kstest(list_mse, cdf='norm', args=(mean_mse , enheraf_mse))

print(p_value , ks_statistic)
plt.show()
