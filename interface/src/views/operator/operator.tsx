import HospitalInfo from "@/components/hospitalInfo/hospitalInfo";
import { Button } from "@/components/ui/button";
import { Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";




const Operator = () => {

    return (
        <>
            <article className="w-[100%] flex flex-row">
                <section className="w-1/2">
                    <Card>
                        <CardHeader>
                            <CardTitle className="text-left">Paient</CardTitle>
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
                            <HospitalInfo totalBeds={100} intransit={20} occupied={50} hospitalName="Burwood hospital" distance={24} />
                        </CardContent>
                    </Card>

                </section>
            </article>
        </>
    )

}


export default Operator;