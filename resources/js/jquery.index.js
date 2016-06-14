	$(function(){
		$('#create_date').datetimepicker({
			//inline: true,
			dateFormat: 'yy-mm-dd',
			timeFormat: "HH:mm:ss",
			maxDate:"+0m +0w"
		});

		uploadImage("#imgTitle","face") ;
        uploadImage("#imgTitleBig","ocr") ;
        uploadImage("#bce","bceocr") ;
        uploadImage("#nude","nude") ;

		$("#autoplay").click(function(){
			var check = $("#autoplay").is(':checked') ;
			if(check){
				$("#playcount").show() ;
			}else{
				$("#playcount").hide() ;
			}
		}) ;

	}) ;
	/**
	 * id:#id
	 * type:存储目录名
	 */
	function uploadImage(id,type){
	    var upload = new AjaxUpload(jQuery(id), {
		    action: '/upload',
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
		        if (ext && /^(gif|jpg|png|jpeg)$/i.test(ext)) {
		            this.setData({
		                'limitMaxSize': '2',
		                'type':type,
		                'key2': '...'
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
					$(id+"_img").html("<img style=\"height:180px\" src=\"/uploads/"+type+"/"+response.filename+"\"/>") ;
					$(id+"_inp").val(file) ;
					$(id+"_filename").val(response.filename) ;
		        }
		        if(response.status == "n"){
		        	alert(response.info) ;
		        }
                if(response.msg &&response.msg!=""){
                    $("#msg").html(unescape(response.msg)) ;
                }
		    }
		});
	}    	


	$(function(){
		
	}) ;


