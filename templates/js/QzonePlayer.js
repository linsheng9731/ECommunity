/**
 *
 * Created by abnerzheng on 15/5/10.
 */

//var height = document.getElementById("div2").clientHeight;
/*ClientHeight:获取对象的高度，不计算任何边距、边框、滚动条，但包括该对象的补白*/

(function () {

    //调用播放器进行播放
    qcVideo.use("startup",
        function (mod) {
            var option = {
                "auto_play": "0",
                "file_id": "16092504232103514425",
                "app_id": "1251439114",
                "width": "100%",
                "height": "400px"
            };
            mod.start(option, "playercontainer", "id_video_container");
        });
})();

