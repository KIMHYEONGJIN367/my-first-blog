#!C:\Anaconda3\Python.exe
import sys
import io
import cgi
#import Test_P
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')

#pnl = 0
print("content-type: text/html; charset-utf-8\n")

print('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="ko">
	<head>
		<meta charset="utf-8">
		<title>毕业设计 - 金亨陈</title>
	</head>
	<body>
		  	<div class="header">
				<h1 align="center">金融数据分析的人机混合智能方法研究</h1>
				<h2 align="right">by 金亨陈</h2>
				<span id="line"></span>
				<hr/>
			</div>

			<div class="body">
			选出需要加入的参数(选项越多计算时间越长）<br>
			<form action='Test_P.py'>
			<input type='checkbox' name='select' value='last_price'>最新成交价
			<input type='checkbox' name='select' value='last_volume'>成交量
			<input type='checkbox' name='select' value='interest'>持仓数<br>
			<input type='checkbox' name='select' value='volume'>累计成交量
			<input type='checkbox' name='select' value='acc_turover'>累计成交金额
			<input type='checkbox' name='select' value='high'>最高<br>
			<input type='checkbox' name='select' value='low'>最低
			<input type='checkbox' name='select' value='open'>起始价
			<input type='checkbox' name='select' value='pre_close'>结束价<br>
			<input type='submit' value='Submit'>
			</form>
			</div>
			
			<div id="color" style="float:left;width:100%;padding:5px">

			</div>

			<div id="y_line" style="float: left; width: 2%; padding:5px;" >
			</div>
			
			<div id="paint" style="padding:0px 0px 0px 50px">
			</div>

			<div id="x_line" style="float:left;width:100%;padding:7px">

			</div>
			<p></p>
			</body>
		</html>
''')

'''
			<!---
			<script>
				var color_table = "<table border = '1' align = 'left'><tr height='50px'>"
				var cc=255,dd=251
				for (c=128;c>=0;c--){			
					if(c>=64){
					color_table+="<td width='2px' style ='background-color:rgb(255,255,"+(cc)+")'></td>";
					cc-=4;							
					}
					else{
					color_table+="<td width='2px' style ='background-color:rgb("+dd+","+dd+",0)'></td>";
					dd-=4;							
					}

				}
				color_table+="</tr></table>";
				color.innerHTML=color_table;
			</script>
			--->

			<script> //Paint Table function
				var btn = document.querySelector('.btn')
				var x = 10
				var y = 10
				function btn_click(){
					var tag = "<table border='1' cellspacing = '5' >";
		      		var x_v = 10;
			    	var y_v = 10;
			    	var tag_x = "<table align = 'left' bgcolor='#ffffff' style='filter:alpha(opacity=80)' cellspacing = '5'> <tr>"
			    	var tag_y = "<table bgcolor='#ffffff' width='20' style='filter:alpha(opacity=80)' cellspacing = '5'>"
			    		
			    		for (k = y_v; k >0 ; k--){
			    			tag_y += "<tr valign = 'top' height='50px'><td>"+k+"</td></tr>"
			    		}
			    		y_line.innerHTML = tag_y+"</table>";
			    		
			    		for (i = 0; i <=x_v ; i++){
			    			tag_x += "<td width='50px' align=right>"+i+"</td>"
			    		}
			    		x_line.innerHTML += tag_x+"</tr></table>";
			    		for (j = 1; j <= y_v; j++) {
			        		tag += "<tr height='50px' align='center'>";
		        				for (i = 1; i <= x_v; i++) {
		          					tag += "<td width='50px'>"+"xx%"+"</td>"
		          				} //Insert value
		       		 		tag += "</tr>";
		       		 		}
		      			tag += "</table>";
		      			paint.innerHTML = tag;
				}
				btn.addEventListener('click',btn_click);
			</script> 
'''

