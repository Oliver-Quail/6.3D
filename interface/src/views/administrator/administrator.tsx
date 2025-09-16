import TransferButton from "@/components/transferButton/transferButton";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import UnitInfo from "@/components/unitInfo/unitinfo";





const Administrator = () => {


    return (
        <article className="w-[100%] flex flex-row">
            <section className="w-[50%]">
                <Card>
                    <CardHeader>
                        <CardTitle className="text-left">Burwood hospital</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <UnitInfo typeOfBed="Emergancy Beds" numberOfBeds={200} />
                        <UnitInfo typeOfBed="Burn unit Beds" numberOfBeds={15} />
                        <UnitInfo typeOfBed="ICU Beds" numberOfBeds={50} />
                        <UnitInfo typeOfBed="Water unit Beds" numberOfBeds={10} />

                    </CardContent>
                </Card>
            </section>
            <section className="w-[50%]">
                <Card>
                    <CardHeader>
                        <CardTitle className="text-left">Tranfers</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <TransferButton />
                    </CardContent>
                </Card>

            </section>
        </article>
    )
}


export default Administrator;