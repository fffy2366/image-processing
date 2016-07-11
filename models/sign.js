var db = require('./db') ;
var _ = require('underscore');
var logger = require('../config/Logger') ;

var Sign = function() {};

Sign.prototype.find = function(id, callback) {
    var sql = "SELECT * FROM sign WHERE sign_id =?";
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            connection.release();
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, [id], function(err, results) {
            logger.info("sql:"+sql) ;
            if (err) {
                callback(true);
                return;
            }
            connection.release();
            callback(false, results);
        });
    });
};
/**
 * 添加
 */
Sign.save = function(username,mobile,address,photo,created_at, callback) {
    logger.info("username:"+username) ;
    var sql = "INSERT INTO sign (username,mobile,address,photo, created_at) VALUES(?,?,?,?,?)";
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            logger.error(err) ;
            connection.release();
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, [username,mobile,address,photo, created_at], function(err, results) {
            logger.info("sql:"+sql) ;
            if (err) {
                logger.error(err) ;
                callback(true);
                return;
            }
            connection.release();
            callback(false, results);
        });
    });
};
/**
 * 更新
 */
Sign.update = function(id, signtitle, callback) {
    logger.info("signtitle:"+signtitle+" id:"+id) ;
    var sql = "UPDATE sign SET title = ?  WHERE sign_id =?";
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            connection.release();
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, [signtitle, parseInt(id)], function(err, results) {
            logger.info("sql:"+sql) ;
            if (err) {
                logger.error(err) ;
                callback(true);
                return;
            }
            connection.release();
            callback(false, results);
        });
    });
};
Sign.findAll = function(callback){
    var sql = "SELECT  * FROM sign WHERE 1=1 AND is_deleted = 0 ";
   
    sql += " ORDER BY created_at ASC " ;
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, function(err, results) {
            //logger.info("sql:"+sql) ;
            if (err) {
                connection.release();
                callback(true);
                return;
            }
			connection.release();
			callback(false, results);            
        });
    });
}
Sign.findAllByPage = function(currPage, pageSize, keywords, callback){
    var currCount = (parseInt(currPage)-1)*pageSize ;
    var sql = "SELECT SQL_CALC_FOUND_ROWS * FROM sign WHERE 1=1 AND is_deleted = 0";
    if(keywords){
        sql += " AND title LIKE '%"+keywords+"%'" ;
    }
    sql += " ORDER BY created_at DESC LIMIT "+currCount+","+pageSize ;
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, function(err, results) {
            logger.info("sql:"+sql) ;
            if (err) {
                connection.release();
                callback(true);
                return;
            }
            var sqlCount = "SELECT FOUND_ROWS() c" ;
            connection.query(sqlCount, function(err, totalCount){
                //console.log(totalCount) ;
                connection.release();
                callback(false, totalCount[0].c, results);
            }) ;
        });
    });    
}
Sign.findById = function(id, callback){
    var sql = "SELECT * FROM sign WHERE sign_id=?";
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            connection.release();
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, [id], function(err, results) {
            logger.info("sql:"+sql) ;
            if (err) {
                callback(true);
                return;
            }
            connection.release();
            callback(false, results);
        });
    });    
}
Sign.deleteById = function(tid, callback){
    logger.info(" tid:"+tid) ;
    var sql = "UPDATE sign SET is_deleted = 1 WHERE sign_id=? ";
    var conditions = [tid] ;
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            connection.release();
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, conditions, function(err, results) {
            logger.info("sql:"+sql) ;
            if (err) {
                logger.info(err) ;
                connection.release();
                callback(true);
                return;
            }
            connection.release();
            callback(false, results);
        });
    });    
}

module.exports = Sign ;
