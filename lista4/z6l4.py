import colorsys
(r, g, b) = (0.8547,0.123,1)
(h, s, v) = colorsys.rgb_to_hsv(r, g ,b)
print ('Hsv to: ', h,s,v)