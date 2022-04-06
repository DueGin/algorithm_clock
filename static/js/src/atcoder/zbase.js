class AtCoder extends Text_Object
{
    constructor(textshow)
    {
        super();
        this.textshow = textshow;
        this.$info = $(`<div class="textshow-textinfo"></div>`);
        this.get_info();
    }

    get_info()
    {
        let outer = this;
        
        $.ajax({
            url : "http://154.86.27.91:8001/oj/get_info/",
            type : "GET",
            data : {
                'platform' : 'atcoder',
            },
            success : function(resp){
                if(resp.result === "success")
                {
                    outer.show(resp)
                }
            }
        })
    }

    show(resp){
        
        let atcoder = resp.atcoder;
        

        for(let i = 0; i < atcoder.length; i++){
            let url = resp.atcoder[i].url;
            let textname = resp.atcoder[i].name;
            let time =  resp.atcoder[i].time;
            let $each_text = $(`
<div href=${url} class="textshow-atcoder-info">
    <div class="textshow-atcoder-info-name">${textname}</div>
    <div class="textshow-atcoder-info-time">${time}</div>
</div>
`);
            this.$info.append($each_text);
        }

        this.textshow.$textshow.append(this.$info);

    }

}