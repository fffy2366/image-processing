/**
 * log4js 日志输出配置文件
 * @type {exports}
 */
var log4js = require('log4js');
var path = require('path') ;
// logger configure
log4js.configure({
    appenders: [
        { type: 'console' }, {
            type: 'dateFile',
            filename: path.dirname()+'/logs/access.log',
            pattern: "_yyyy-MM-dd",
            maxLogSize: 1024/2,
            alwaysIncludePattern: false,
            backups: 5,
            //category: 'logger',
            category: 'normal' 
        }
    ],
    replaceConsole: true
});


var logger = log4js.getLogger('normal');
//logger.setLevel('TRACE');
logger.setLevel('DEBUG');
//logger.setLevel('INFO');
//logger.setLevel('WARN');
//logger.setLevel('ERROR');
//logger.setLevel('FATAL');



module.exports = logger;