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

    const [hospitalInfo, setHospitalInfo] = useState<Record<string, hospitalInfoData>>({})
    const [hospitals, setHospitals] = useState<string[]>([])

    useEffect(() => {
        if(Object.keys(hospitalInfo).length == 0) {
            let temp :Record<string, hospitalInfoData> = {}
            Object.values(HOSPITALS).forEach(element => {
                if(element != HOSPITALS.BURWOOD) {
                    getHospitalInfo({hospitalInfo :hospitalInfo, setHospitalInfo :setHospitalInfo, targetHospital: element})
                }
            });
            setHospitals(Object.keys(hospitalInfo))
        }
        console.log(hospitalInfo)

    })

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
                                Object.keys(hospitalInfo).map((key) => {
                                    return (
                                        <HospitalInfo totalBeds={hospitalInfo[key].total_beds} intransit={hospitalInfo[key].in_transit} occupied={hospitalInfo[key].occupied} hospitalName={hospitalInfo[key].name} distance={22} />
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