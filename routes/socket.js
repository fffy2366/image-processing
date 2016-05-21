/*
 * GET socket page.
 */
var express = require('express');
var http = require('http');

/**
 * [Socket.io在线聊天室](http://blog.fens.me/nodejs-socketio-chat/)
 * [node.js中Socket.IO的进阶使用技巧](http://www.jb51.net/article/57091.htm)
 * [Server API](http://socket.io/docs/server-api/)
 *
 *
 * @param app
 * @param server
 */
module.exports = function(app,server) {
    var io = require('socket.io').listen(server);

    io.sockets.on('connection', function(socket) {
        //把信息从Redis发送到客户端
        socket.on('message', function(message){
            console.log(message) ;
            socket.emit("message",message);
        });
    }) ;
} ;
