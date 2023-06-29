# epic7shopScript
第七史诗刷商店脚本，前台python图像识别，随机范围坐标点击防检测

编写环境：
Win11 BlueStacks 国际版 ; 显示器分辨率 2560×1600 ；模拟器分辨率 1920×1080（开全屏） ；第七史诗国服

参照https://github.com/dengpris/E7-Secret-Shop-Auto-Refresher

# 快速使用
python 安装以下库（可使用anaconda虚拟环境）
```
pip install keyboard
pip install opencv-python
pip install pyautogui
pip install mouse
pip install pillow
pip install pywin32
```
运行脚本，输入分钟数，或者使用IDE运行（例如PyCharm）
```
python Auto.py
```

# 调整说明
由于分辨率大小引起的位置差异需要自行调整，可以使用pyautogui等获取坐标对个人电脑上进行微调（示例testpos.py）
1.识别书签后根据书签图片中心位置与购买按钮的差值进行计算点击购买，需要获取该差值，在如下位置更改1100和40数值。
```
Line36  click(pos_point[0]+1100+rand_x, pos_point[1]+40+rand_y)
```
2.图片可能识别不准，我从参考的修改过来的时候（那边是英文版）识别不了书签，重新截图后能够识别。如果你有这个问题可以手动操作商店截图并替换项目中的图片。
Q&A：如何判断识别不能？
如果你会调试，打个断点在获取坐标的代码后一行查看坐标是否为None就知道。如下所示代码：
```
Line 108  Coven_pos=pyautogui.locateOnScreen('covenant.png',confidence=0.8)
```
3.滑动的随机坐标值的调整，如下代码中（124行）1453与1878的数值替换为不会点到商品图片和购买键中间的一个x坐标区间就行。
```
  #Scroll down
      time.sleep(random.uniform(0.2, 0.4))
      scroll_pt_x = random.randint(1453,1878)
      scroll_pt_y = random.randint(400,680)
```
