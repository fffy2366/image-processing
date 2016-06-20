/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Version : 50623
 Source Host           : localhost
 Source Database       : images

 Target Server Version : 50623
 File Encoding         : utf-8

 Date: 06/20/2016 16:54:03 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `images`
-- ----------------------------
DROP TABLE IF EXISTS `images`;
CREATE TABLE `images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `is_face` tinyint(2) NOT NULL DEFAULT '0' COMMENT '是否人脸',
  `ocr` varchar(255) NOT NULL COMMENT '文字识别结果',
  `is_qq` tinyint(2) NOT NULL DEFAULT '0' COMMENT '是否qq，含四个数字',
  `is_nude` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否黄色图片',
  `created_at` datetime NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9634 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `similar_images`
-- ----------------------------
DROP TABLE IF EXISTS `similar_images`;
CREATE TABLE `similar_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `features` text NOT NULL COMMENT '文字识别结果',
  `created_at` datetime NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_index` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
