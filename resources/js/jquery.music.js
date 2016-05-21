$(function(){
	bindPlay() ;
	uploadMusic("#music","musics") ;
}) ;
function bindPlay(){
	// 通过全局变量的方式初始化
	var player = window.player = new _mu.Player({
	        mode: 'list',
	        baseDir: '/public/dist'
	    }),
	    $pl = $('#playlist-demo'),
	    reset = function() {
	        $pl.find('> li').removeClass('playing pause')
	            .find('.time').remove();
	    },
	    findCurrItem = function() {
	        var link = player.getCur();
	        link = link.substring(link.indexOf('/public/uploads/musics/'));
	        return $pl.find('[data-link="' + link + '"]');
	    },
	    $time = $('<span class="time"></span>');
	
	$pl.on('click', '> li', function() {
	    var $this = $(this);
	    if ($this.hasClass('playing')) {
	        player.pause();
	    } else {
	        player.reset().add($this.data('link')).play();
	    }
	});
	
	$pl.on('click','> li a',function(e){
		$this = $(this) ;
        var link = $this.parent().attr("data-link");
        link = link.replace('/public/uploads/musics/','');
        $.post('/admin/music/delete',{'file':link},function(data){
			if(data.status=="y"){
				$this.parent().remove() ;
			}        	
        }) ;
		e.stopPropagation();
	}) ;
	
	player.on('playing pause', function() {
	    reset();
	    findCurrItem().addClass(player.getState()).append($time);
	}).on('ended', reset).on('timeupdate', function() {
	    $time.text(player.curPos(true) + ' / ' + player.duration(true));
	});
}
/**
 * 上传音乐
 * id:#id
 * type:存储目录名
 */
function uploadMusic(id,type){
    var upload = new AjaxUpload(jQuery(id), {
	    action: '/admin/music/upload',
	    name: 'upfile',
	    data: {
	        'limitMaxSize': "1"
	    },
	    autoSubmit: true,
	    responseType: 'json',
	    onChange: function(file, ext){
	    },
	    onSubmit: function(file, ext){
	        // Allow only images. You should add security check on the server-side.
	        if (ext && /^(mp3)$/i.test(ext)) {                            
	            this.setData({
	                'limitMaxSize': '2',
	                'type':type,
	                'key2': '...',
	                'pid':pid
	            });
	            //loading
	            $(id+"_loading").html("<img src=\"/resources/js/fileuploader/loading.gif\"/>") ;
	        } else {
	            alert("上传文件类型不正确") ;
	            return false;
	        }                            
	    },
	    onComplete: function(file, response){
	        //this.disable();
	        //loading
	        $(id+"_loading").empty() ;
	        
	        if(response.status == "y"){
				$(id+"_img").html("上传成功") ;
				$(id+"_inp").val(file) ;
				$(id+"_filename").val(response.filename) ;
				$("#playlist-demo").prepend('<li data-link="/public/uploads/musics/'+response.filename+'"  class="pause"><i class="play-btn"></i>'+file+' <a class="icon-remove"></a></li>') ;
				//bindPlay() ;
	        }
	        if(response.status == "n"){
	        	alert("上传失败") ;
	        }
	    }
	});
}  