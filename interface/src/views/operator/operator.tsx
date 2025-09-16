import HospitalInfo from "@/components/hospitalInfo/hospitalInfo";
import { Button } from "@/components/ui/button";
import { Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import HOSPITALS from "@/misc/url";
import getHospitalInfo from "@/services/fetching";
import hospitalInfoData from "@/types/hospitalInfoData";
import { useEffect, useState } from "react";




const Operator = () => {

    const [hospitalInfo, setHospitalInfo] = useState<hospitalInfoData[]>([])

    useEffect(() => {
        getHospitalInfo({hospitalInfo :hospitalInfo, setHospitalInfo :setHospitalInfo, targetHospital: HOSPITALS.BURWOOD})
        
        console.log(hospitalInfo)

    }, [])

    return (
        <>
            <article className="w-[100%] flex flex-row">
                <section className="w-1/2">
                    <Card>
                        <CardHeader>
                            <CardTitle className="text-left">Paient</CardTitle>
                            <CardDescription className="text-left">91 Colbert Avenue</CardDescription>
                        </CardHeader>
                        <CardContent>
                            
                            <Label htmlFor="Notes">Notes on paitent</Label>
                            <Textarea placeholder="Notes" id="Notes" />
                            <section className="mt-5">
                                <Button className="w-[50%]" variant="destructive">Cancel</Button>
                                <Button className="w-[50%]">Confirm</Button>
                            </section>
                        </CardContent>
                    </Card>
                </section>
                <section className="w-1/2">
                    <Card>
                        <CardHeader>
                            <CardTitle className="text-left">Hospitals</CardTitle>
                        </CardHeader>
                        <CardContent>
                            {
                                hospitalInfo.map((key) => {
                                    return (
                                        <HospitalInfo totalBeds={key.total_beds} intransit={key.in_transit} occupied={key.occupied} hospitalName={key.name} distance={Math.random()} />
                                    )
                                })
                            }
                        </CardContent>
                    </Card>

                </section>
            </article>
        </>
    )

}


export default Operator;