var mysql = require('mysql');
var config = require('../config/settings');
if(config.env=="dev"){
    var pool = mysql.createPool(config.mysql_dev);
}else if(config.env=="testing"){
    var pool = mysql.createPool(config.mysql_testing);
}else if(config.env=="prod"){
    var pool = mysql.createPool(config.mysql_prod);
}
/**
 * get a connection from the pool
 */
pool.getconnect = function(){
    var Q = require("q");
    var deferred = Q.defer();
    // get a connection from the pool
    pool.getConnection(function(err, connection) {
        if (err) {
            deferred.reject(new Error(err));
            connection.release();
        }else{
            deferred.resolve(connection);
        }
    }) ;
    return deferred.promise;
} ;

pool.find = function(connection,sql,conditions){
    var Q = require("q");
    var deferred = Q.defer();
    connection.query(sql, conditions, function(err, results) {

        //logger.info("sql:"+sql) ;
        if (err) {
            //logger.info(err) ;
            deferred.reject(new Error(err));
            connection.release();
        }else{
            deferred.resolve(results);
        }
        connection.release();

    });
    return deferred.promise;
} ;
exports.pool = pool;
