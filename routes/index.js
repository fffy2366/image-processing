var express = require('express');
var router = express.Router();
var fs = require('fs') ;

var multiparty = require('multiparty');
var StringUtils = require('../components/StringUtils') ;
var uuid = require('node-uuid') ;
var shelljs = require('shelljs');
var Sign = require('../models/sign')
var moment = require('moment');

/* GET home page. */
router.get('/', function(req, res, next) {
    console.log(__dirname) ;
  res.render('index', { title: 'Express' });
});
router.get('/socket', function (req, res) {
    res.render('socket');
});

/**
 * www.npmjs.com/package/multiparty
 */
router.post('/upload',function(req,res){
    var form = new multiparty.Form();
//        res.setHeader('Content-Type','text/html');
//        res.setHeader('charset','utf-8');
    form.parse(req, function(err, fields, files) {
        //res.writeHead(200, {'content-type': 'text/plain'});
        //res.write('received upload:\n\n');
        console.log(fields) ;
        console.log(files) ;
        //res.end(util.inspect({fields: fields, files: files}));
        var limitMaxSize = fields.limitMaxSize ;
        var type = fields.type ;
        //StringUtils.mkdir('./public/uploads/'+type, function(err) {console.log(err);});
        console.log("limitMaxSize:"+limitMaxSize) ;
        console.log("type:"+type) ;
        StringUtils.mkdirSync('../public/uploads/' + type);
        if(err){
            console.log("err:"+err) ;
            //res.send({status: "n", info: "上传失败"});
        }
        var upfile = files.upfile ;
        console.log("length:"+upfile.length) ;
        for (var i = 0; i < upfile.length; i++) {
            var file = upfile[i];
            console.log("file" + file);
            //console.log(file) ;
            //console.log(file.headers) ;
            var name = file.originalFilename ;
            var fileSize = file.size ;
            console.log("name:"+name) ;
            console.log("fileSize:"+fileSize) ;
            var src_path = file.path;
            var ext = name.split(".");
            if (ext.length > 1) {
                ext = ext[1];
            }
            console.log("ext:" + ext);
            //var target_path = path.join(path.dirname(__dirname), "/public/uploads/" + name) ;
            //var target_path = "./public/uploads/questions/" + name ;
            var newFile = uuid.v1() + "." + ext;
            var target_path = "./public/uploads/" + type + "/" + newFile;
            console.log("target_path:" + target_path);
            console.log("src_path:" + src_path);

            fs.rename(src_path, target_path, function (err) {
                res.setHeader('Content-Type','text/html');
                res.setHeader('charset','utf-8');
                if (err) {
                    console.log("err:"+err) ;
                    res.send({status: "n", info: "上传失败"});
                }
                console.log("i:" + i);//为啥i=1
                if(type=="face"){
                    /*if (shelljs.exec('cd '+__dirname+'/..'+' && python face.py '+newFile).code !== 0) {
                        shelljs.echo('Error: failed');
                        res.send({status: "n", info: "失败", "path": target_path, "filename": newFile});
                    } else {
                        shelljs.echo('success');
                        res.send({status: "y", info: "上传成功", "path": target_path, "filename": "f_"+newFile});
                    }*/
                    var exec = require('child_process').exec;
                    var cmd = 'cd '+__dirname+'/..'+' && python face.py '+newFile ;
                    console.log("cmd:"+cmd) ;
                    var child = exec(cmd, function(err, stdout, stderr) {
                        if (err) {
                            console.log(err) ;
                            res.send({status: "n", info: "失败", "path": target_path, "filename": newFile});
                        }
                        console.log(stdout);
                        res.send({status: "y", info: "上传成功", "path": target_path, "filename": "f_"+newFile,"msg":escape(stdout)});
                    });
                }
                if(type=="ocr"){
                    var exec = require('child_process').exec;
                    var cmd = 'cd '+__dirname+'/..'+' && python ocr.py '+newFile ;
                    console.log("cmd:"+cmd) ;
                    var child = exec(cmd, function(err, stdout, stderr) {
                        if (err) {
                            console.log(err) ;
                            res.send({status: "n", info: "失败", "path": target_path, "filename": newFile});
                        }
                        console.log(stdout);
                        res.send({status: "y", info: "上传成功", "path": target_path, "filename": newFile,"msg":escape(stdout)});
                    });

                }
                if(type=="bceocr"){
                    var exec = require('child_process').exec;

                    var child = exec('cd '+__dirname+'/..'+' && python bceocr.py '+newFile, function(err, stdout, stderr) {
                        if (err) {
                            console.log(err) ;
                            res.send({status: "n", info: "失败", "path": target_path, "filename": newFile});
                        }
                        console.log(stdout);
                        res.send({status: "y", info: "上传成功", "path": target_path, "filename": newFile,"msg":escape(stdout)});
                    });

                }
                if(type=="nude"){
                    var exec = require('child_process').exec;

                    var child = exec('cd '+__dirname+'/..'+' && python nudedetect.py '+newFile, function(err, stdout, stderr) {
                        if (err) {
                            console.log(err) ;
                            res.send({status: "n", info: "失败", "path": target_path, "filename": newFile});
                        }else{
                            console.log(stdout);
                            res.send({status: "y", info: "上传成功", "path": target_path, "filename": newFile,"msg":escape(stdout)});
                        }
                    });

                }
                if(type=="similar"){
                    var exec = require('child_process').exec;
                    var shell = 'cd '+__dirname+'/../bin/python'+' && python search_one.py --dataset ../../public/uploads/similar --index ../../public/uploads/similar.cpickle --query '+newFile
                    var child = exec(shell, function(err, stdout, stderr) {
                        if (err) {
                            console.log(err) ;
                            res.send({status: "n", info: "失败", "path": target_path, "filename": newFile});
                        }else{
                            console.log(stdout);
                            res.send({status: "y", info: "上传成功", "path": target_path, "filename": newFile,"msg":escape(stdout)});
                        }
                    });

                }
                if(type=="photo"){
                    res.send({status: "y", info: "上传成功", "path": target_path, "filename": newFile});
                }

            });
        }
    });


}) ;

router.get('/shell', function(req, res) {
    if (shelljs.exec('cd ~/python/image-processing && python face.py 2e66ebc0-1f3a-11e6-89c9-ddb2ad1cd177.jpg').code !== 0) {
        shelljs.echo('Error: failed');
        res.send("Error: failed");
    } else {
        shelljs.echo('success');
        res.send("success");
        //var sleep = require('sleep');
        //sleep.sleep(3)
        //shelljs.exec('pm2 restart 0');
    }
});

var Pluploader = require('node-pluploader');

var pluploader = new Pluploader({
    uploadLimit: 6 //单个文件最大，MB
    //uploadDir: '/Users/fengxuting/python/image-processing/public/uploads/similar'
});

 /*
  * Emitted when an entire file has been uploaded.
  *
  * @param file {Object} An object containing the uploaded file's name, type, buffered data & size
  * @param req {Request} The request that carried in the final chunk
  */
pluploader.on('fileUploaded', function(file, req) {
    StringUtils.mkdirSync('../public/uploads/similar');
    var target_path = "./public/uploads/similar/"+file.name
    fs.writeFile(target_path, file.data,function(err){
        console.log(file);
        var exec = require('child_process').exec;
        var shell = 'cd '+__dirname+'/../bin/python'+' && python search_index_one.py --dataset ../../public/uploads/similar --index ../../public/uploads/similar.cpickle --file '+file.name
        console.log(shell) ;
        var child = exec(shell, function(err, stdout, stderr) {
            if (err) {
                console.log(err) ;

            }
            console.log(stdout);

        });
    }) ;

});

/*
  * Emitted when an error occurs
  *
  * @param error {Error} The error
  */
pluploader.on('error', function(error) {
    throw error;
});

// This example assumes you're using Express
router.post('/plupload', function(req, res){
  pluploader.handleRequest(req, res);
});
/**
 * 图片检测
 * https://cnodejs.org/topic/4f939c84407edba2143c12f7
 */
router.post('/detect', function(req, res){
    //接收前台POST过来的base64
    var imgData = req.body.imgData;
    //过滤data:URL
    var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
    var dataBuffer = new Buffer(base64Data, 'base64');
    fs.writeFile("out.png", dataBuffer, function(err) {
        if(err){
            res.send(err);
        }else{
            res.send("保存成功！");
        }
    });
});
/**
 * 聚会报名
 */
router.get('/sign', function(req, res){
    res.render('sign', { title: 'Express' });
});
/**
 * 姓名  电话  常住城市   上传一张个人近照
 */
router.post('/sign', function(req, res){
    var username = req.body.username ;
    var mobile = req.body.mobile ;
    var address = req.body.address ;
    var photo = req.body.photo ;
    var created_at = moment().format("YYYY-MM-DD HH:mm:ss") ;
    Sign.save(username,mobile,address,photo,created_at,function(err,result){
        if(err){
            res.send({status: "n", info: "报名失败" });
        }else{
            res.send({status: "y", info: "报名成功" });
        }
    }) ;

});

module.exports = router;
