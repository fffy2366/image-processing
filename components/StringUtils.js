/**
 * 字符串处理
 * @type {exports}
 */
var fs = require('fs') ; 
var path = require('path') ; 
var StringUtils = {};
//异步的实现
StringUtils.mkdir = function(dirpath, mode, callback) {
    if(arguments.length === 2) {
        callback = mode;
        mode = 0777;
    }
	console.log("dirpath:"+dirpath) ;
    fs.exists(dirpath, function(exists) {
        if(exists) {
            callback(null);
        } else {
            StringUtils.mkdir(path.dirname(dirpath), mode, function(err) {
                // console.log('>>', dirpath)
                if(err) return callback(err);
                fs.mkdir(dirpath, mode, callback);
            });
        }
    });
};
//同步的实现
StringUtils.mkdirSync = function(dirpath, mode) {
    dirpath.split('\/').reduce(function(pre, cur) {
        var p = path.resolve(pre, cur);
        if(!fs.existsSync(p)) fs.mkdirSync(p, mode || 0755);
        return p;
    }, __dirname);
};
StringUtils.getClientIp = function(req) {
    var ipAddress;
    var forwardedIpsStr = req.header('x-forwarded-for'); 
    if (forwardedIpsStr) {
        var forwardedIps = forwardedIpsStr.split(',');
        ipAddress = forwardedIps[0];
    }
    if (!ipAddress) {
        ipAddress = req.connection.remoteAddress;
    }
    return ipAddress;
};
StringUtils.removeFile = function(file,callback){
	fs.exists(file, function(exists) {
        if(exists) {
        	fs.unlinkSync(file);
            callback("success");
        }else{
        	callback("nofile") ;
        }
	});
} ;
/**
 * 返回两个数之间的随机数
 * @param Min
 * @param Max
 * @returns {*}
 * @constructor
 */
StringUtils.GetRandomNum = function(Min, Max) {
    var Range = Max - Min;
    var Rand = Math.random();
    return(Min + Math.round(Rand * Range));
} ;
/**
 * abcd 转成1234
 * @param str
 * @returns {string}
 * @constructor
 */
StringUtils.char2num = function(str){
    str = str.toUpperCase() ;
    var arr = str.split("") ;
    var num = [] ;
    for(var s in arr){
        switch (arr[s]){
            case 'A':
                num.push(1) ;
                break ;
            case 'B':
                num.push(2) ;
                break ;

            case 'C':
                num.push(3) ;
                break ;
            case 'D':
                num.push(4) ;
                break ;
        }
    }
    return num.join(" ") ;
} ;
/**
 * 数组返回随机的几个不重复的数
 * @param arr
 * @param num
 * @returns {Array}
 */
StringUtils.getArrayItems = function(arr, num) {
    //新建一个数组,将传入的数组复制过来,用于运算,而不要直接操作传入的数组;
    var temp_array = new Array();
    for (var index in arr) {
        temp_array.push(arr[index]);
    }
    //取出的数值项,保存在此数组
    var return_array = new Array();
    for (var i = 0; i<num; i++) {
        //判断如果数组还有可以取出的元素,以防下标越界
        if (temp_array.length>0) {
            //在数组中产生一个随机索引
            var arrIndex = Math.floor(Math.random()*temp_array.length);
            //将此随机索引的对应的数组元素值复制出来
            return_array[i] = temp_array[arrIndex];
            //然后删掉此索引的数组元素,这时候temp_array变为新的数组
            temp_array.splice(arrIndex, 1);
        } else {
            //数组中数据项取完后,退出循环,比如数组本来只有10项,但要求取出20项.
            break;
        }
    }
    return return_array;
}
module.exports = StringUtils;