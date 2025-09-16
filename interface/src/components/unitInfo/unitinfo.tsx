import { Button } from "../ui/button"
import { Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle } from "../ui/card"


interface uniInfoProps {
    typeOfBed :string;
    numberOfBeds :number;
}


const UnitInfo = (props :uniInfoProps) => {
    return (
        <Card className="my-2">
            <CardHeader>
                <CardTitle className="text-left">{props.typeOfBed}</CardTitle>
                <CardAction>
                    <Button>Edit</Button>
                </CardAction>
                <CardDescription>
                    <p className="text-left">Number of beds: {props.numberOfBeds}</p>
                </CardDescription>
            </CardHeader>
        </Card>
    )
}


export default UnitInfo