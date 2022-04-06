export class Algo
{
    constructor(id)
    {
        this.id = id;
        this.$algo = $('#' + id);

        this.textshow = new TextShow(this);
    }
}
