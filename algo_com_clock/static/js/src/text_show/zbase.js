let text_list = []
class TextShow
{
    constructor(root)
    {
        this.root = root;

        this.$textshow = $(`<div class="textshow"></div>`);

        this.$info = $(`<div class="textshow-textinfo"></div>`);

        this.get_info("atcoder");
        this.get_info("nowcoder");
        
        this.end();

    }

    

    get_info(platform)
    {
        let outer = this;

        $.ajax({
            url : "http://154.86.27.91:8001/oj/get_info/",
            type : "GET",
            data : {
                'platform' : platform,
            },
            success : function(resp){
                if(resp.result === "success")
                {
                    outer.show(resp);
                }
            }
        })
    }

    show(resp){
        let outer = this;
        let info = resp.info;
        
        let $info = $(`<div class="textshow-textinfo"></div>`);

        for(let i = 0; i < info.length; i++){
            let url = resp.info[i].url;
            let textname = resp.info[i].name;
            let time =  resp.info[i].time;
            let $each_text = $(`
<a href=${url} target="_blank">
    <div  class="textshow-info" >
        <div class="textshow-info-name">${textname}</div>
        <div class="textshow-info-time">Time: ${time}</div>
    </div>
</a>
`);
            
            text_list.push($each_text);
            $info.append($each_text);
        }
        // console.log(text_list);
        this.$textshow.append($info);

    }

    end()
    {
        this.root.$algo.append(this.$textshow);
    }


}
