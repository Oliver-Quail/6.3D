import { Card, CardAction, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";




const TransferButton = () => {


    return (
        <Card>
            <CardHeader>
                <CardTitle className="text-left">Burwood to Bendigo</CardTitle>
                <CardDescription className="text-left">
                    Transfer 38 paitents from Burwood to Bendigo
                </CardDescription>
                <CardAction>
                    <Button>Confirm Transfer</Button>
                </CardAction>
            </CardHeader>
        </Card>
    )
}

export default TransferButton;