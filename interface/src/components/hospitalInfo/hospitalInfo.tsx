import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardAction } from "@/components/ui/card";
import { Button } from "../ui/button";


interface hospitalProps {
    totalBeds :number;
    intransit :number;
    occupied :number;
    hospitalName :string;
    distance: number
    has_burn_unit :number
    has_icu :number
    has_water_unit :number
}



const HospitalInfo = (props :hospitalProps) => {

    let avaliable :number = props.totalBeds - props.occupied - props.intransit
    
    return (
        <Card className="mt-3">
            <CardHeader>
                <CardTitle className="text-left">{props.hospitalName} ({props.distance} km)</CardTitle>
                <CardDescription className="text-left">
                    <section>
                        <section className="flex items-center">
                            <ion-icon name={avaliable > 0 ? 'checkmark-outline' : 'close-outline'}></ion-icon>
                            <p className={avaliable > 0 ? "text-green-500" : "text-red-500"} >{avaliable > 0 ? "Beds are avaliable" : "Beds not are avaliable"}</p>
                            
                        </section>
                    </section>
                </CardDescription>
                <CardAction>
                    <Button>Assign</Button>
                </CardAction>
            </CardHeader>
            <CardContent>
                <section className="text-left">
                    <h3>Avaliable services</h3>
                    <ion-icon name='flame-outline' className={props.has_burn_unit > 0 ? "initial" : 'hidden'}></ion-icon>
                    <ion-icon name='skull-outline' className={props.has_icu > 0 ? "initial" : 'hidden'}></ion-icon>
                    <ion-icon name='water-outline' className={props.has_water_unit > 0 ? "initial" : 'hidden'}></ion-icon>
                </section>
                <h3 className="text-left mt-5">Beds</h3>
                <section className="flex justify-between">
                    <section className="flex items-center">
                        {/* {In transit} */}
                        <ion-icon name="bed-outline"></ion-icon>
                        <p>{avaliable}</p>
                    </section> 
                    <section className="flex items-center">
                        {/* {Total beds} */}
                        <ion-icon name="medkit-outline"></ion-icon>
                        <p>{props.totalBeds}</p>
                    </section>
                    <section className="flex items-center">
                        {/* {In transit} */}
                        <ion-icon name="car-outline"></ion-icon>
                        <p>{props.intransit}</p>
                    </section>
                </section>
            </CardContent>
        </Card>

    )
}

export default HospitalInfo