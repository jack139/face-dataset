# -*- coding: utf-8 -*-

# unpack faces_glintasia dataset
# https://github.com/deepinsight/insightface/wiki/Dataset-Zoo#asian-celeb-94k-ids28m-images8-recommend
#

import os
import mxnet as mx

root_path = './glint_asia'

os.mkdir(root_path)

record = mx.recordio.MXIndexedRecordIO('train.idx', 'train.rec', 'r')

print('read')

label = -1

for i in range(len(record.keys)):
	header, data = mx.recordio.unpack(record.read_idx(i))

	if len(data)==0:
		continue

	if int(header.label[0])!=int(label):
		label = '%d'%(header.label[0])
		print(label)
		os.mkdir(root_path+'/'+label)

	with open('%s/%s/%s.jpg'% (root_path, label, int(header.id)), 'wb') as f:
		f.write(data)

print('done.')
