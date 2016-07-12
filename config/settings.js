module.exports = {
    cookieSecret:'exambyfrank',
    cookieName:'exambyfrank',
    env:"dev",
    mysql_dev: {
        host: 'localhost',

        user: 'root',
        password: '1234',
        database: 'images',
        connectionLimit: 10,
        charset: 'utf8_general_ci',
        supportBigNumbers: true
    },
    mysql_testing: {
        host: '180.76.143.82',
        user: 'images',
        password: 'db2016',
        database: 'images',
        connectionLimit: 10,
        charset: 'utf8_general_ci',
        supportBigNumbers: true
    },
    mysql_prod: {
        host: '127.0.0.1',
        user: 'root',
        password: 'db2016',
        database: 'images',
        connectionLimit: 10,
        charset: 'utf8_general_ci',
        supportBigNumbers: true
    },
    dev:{
        url:'http://localhost:3000'
    },
    testing:{
        url:'http://180.76.143.82:3000'
    },
    prod:{
        url:'http://localhost:3000'
    },
    youyuan_key:'N6AG2WHLH74S5WC5m2'


};
