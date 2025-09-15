import { Card, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

const Login = () => {

    

    return (
        <article className="h-[100dvh]"> 
            <Card className="my-auto w-100 mx-auto">
                <CardHeader>
                    <CardTitle>Victorian Health Load Balancer</CardTitle>
                </CardHeader>
                
                <Input type="text" className="text-center w-8/10 mx-auto" placeholder="User Name" />
                <Input type="password" className="text-center w-8/10 mx-auto" placeholder="Password" />

                <CardFooter>
                    <Button>Login</Button>
                </CardFooter>
                
            </Card>
        </article>
    )
}


export default Login;