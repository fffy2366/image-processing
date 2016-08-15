var db = require('./db') ;
var _ = require('underscore');
var logger = require('../config/Logger') ;

var YouyuanImages = function() {};

YouyuanImages.prototype.find = function(id, callback) {
    var sql = "SELECT * FROM youyuan_images WHERE youyuan_images_id =?";
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
YouyuanImages.save = function(img_id,img_link, created_at, callback) {
    logger.info("img_id:"+img_id) ;
    var sql = "INSERT INTO youyuan_images (img_id,img_link, created_at) VALUES(?,?,?)";
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            logger.error(err) ;
            connection.release();
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, [img_id,img_link, created_at], function(err, results) {
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
YouyuanImages.update = function(id, youyuan_imagestitle, callback) {
    logger.info("youyuan_imagestitle:"+youyuan_imagestitle+" id:"+id) ;
    var sql = "UPDATE youyuan_images SET title = ?  WHERE youyuan_images_id =?";
    // get a connection from the pool
    db.pool.getConnection(function(err, connection) {
        if (err) {
            connection.release();
            callback(true);
            return;
        }
        // make the query
        connection.query(sql, [youyuan_imagestitle, parseInt(id)], function(err, results) {
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
YouyuanImages.findAll = function(callback){
    var sql = "SELECT  * FROM youyuan_images WHERE 1=1 AND is_deleted = 0 ";
   
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
YouyuanImages.findAllByPage = function(currPage, pageSize, keywords, callback){
    var currCount = (parseInt(currPage)-1)*pageSize ;
    var sql = "SELECT SQL_CALC_FOUND_ROWS * FROM youyuan_images WHERE 1=1 AND is_deleted = 0";
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
YouyuanImages.findById = function(id, callback){
    var sql = "SELECT * FROM youyuan_images WHERE youyuan_images_id=?";
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
YouyuanImages.deleteById = function(tid, callback){
    logger.info(" tid:"+tid) ;
    var sql = "UPDATE youyuan_images SET is_deleted = 1 WHERE youyuan_images_id=? ";
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

module.exports = YouyuanImages ;
