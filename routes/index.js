var express = require('express');
var router = express.Router();
var fs = require('fs') ;

var multiparty = require('multiparty');
var StringUtils = require('../components/StringUtils') ;
var uuid = require('node-uuid') ;
var shell = require('shelljs');

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
                    if (shell.exec('cd '+__dirname+'/..'+' && python face.py '+newFile).code !== 0) {
                        shell.echo('Error: failed');
                        res.send({status: "n", info: "失败", "path": target_path, "filename": newFile});
                    } else {
                        shell.echo('success');
                        res.send({status: "y", info: "上传成功", "path": target_path, "filename": "f_"+newFile});
                    }
                }
                if(type=="ocr"){
                    var exec = require('child_process').exec;
                    var cmd = 'cd '+__dirname+'/..'+' && python ocr.py '+newFile+' -psm 6' ;
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
                            res.send({status: "y", info: "上传成功", "path": target_path, "filename": "nude_"+newFile,"msg":escape(stdout)});
                        }
                    });

                }

            });
        }
    });


}) ;

router.get('/shell', function(req, res) {
    if (shell.exec('cd ~/python/image-processing && python face.py 2e66ebc0-1f3a-11e6-89c9-ddb2ad1cd177.jpg').code !== 0) {
        shell.echo('Error: failed');
        res.send("Error: failed");
    } else {
        shell.echo('success');
        res.send("success");
        //var sleep = require('sleep');
        //sleep.sleep(3)
        //shell.exec('pm2 restart 0');
    }
});

module.exports = router;
