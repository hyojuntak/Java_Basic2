package JC;

public class BrandTv extends Tv {
    
    String brand; 

    public BrandTv(int intValue, String strValue){
        //부모가 가지고 있는 channel 변수에 값을 할당한다.
        super.channel = intValue;
        this.brand = strValue;
    }

    public static void main(String[] args) {
        
        BrandTv objTv = new BrandTv(11, "삼성TV");
        objTv.channelUp();  //접근 가능
        ///objTv.chnneldown(); //접근 불가능 
        System.out.println(objTv.brand + "현재 채널은"+ objTv.channel + "번입니다.");
    }
}