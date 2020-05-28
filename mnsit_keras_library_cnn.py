#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist


# In[2]:


(x_train, y_train), (x_test, y_test) = mnist.load_data()


# In[3]:


img=x_train[0]


# In[4]:


img.shape


# In[5]:


img1D=img.reshape(28*28)


# In[6]:


img1D.shape


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


plt.imshow(img)


# In[9]:


x_train1D=x_train.reshape(-1,28*28)


# In[10]:


x_train1D.shape


# In[11]:


x_train=x_train1D.astype('float32')


# In[12]:


from keras.utils.np_utils import to_categorical


# In[13]:


y_train_cat = to_categorical(y_train)


# In[14]:


from keras.models import Sequential


# In[15]:


from keras.layers import Dense


# In[16]:


model = Sequential()


# In[17]:


model.add(Dense(units=512, input_dim=28*28, activation='relu'))


# In[18]:


model.summary()


# In[19]:


model.add(Dense(units=256, activation='relu'))


# In[20]:


model.add(Dense(units=128, activation='relu'))


# In[21]:


model.add(Dense(units=32, activation='relu'))


# In[22]:


model.summary()


# In[23]:


model.add(Dense(units=10, activation='softmax'))


# In[24]:


model.summary()


# In[25]:


from keras.optimizers import RMSprop


# In[26]:


model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )


# In[27]:


h = model.fit(x_train, y_train_cat, epochs=1)


# In[29]:


X_test_1d=x_test.reshape(-1, 28*28)


# In[35]:


X_test=x_train1D.astype('float32')


# In[36]:



y_test_cat=to_categorical(y_test)


# In[37]:


model.predict(X_test)


# In[38]:


y_test_cat


# In[61]:


model.save('mnsitmodel.h1')



# In[ ]:
accuarcy=(h.history['accuracy'])


a=h.history['accuracy'][0]


print("accuarcy is=",a)


with open('/home/ashutosh/Documents/MLworkshop/MLproject/acuuarcy.txt ', 'w+') as output_file:
    output_file.write(str(a))




