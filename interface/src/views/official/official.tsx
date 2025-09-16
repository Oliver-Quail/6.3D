import HospitalInfo from "@/components/hospitalInfo/hospitalInfo";
import TransferButton from "@/components/transferButton/transferButton";
import { Button } from "@/components/ui/button";
import { Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { ChartContainer, ChartConfig, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import HOSPITALS from "@/misc/url";
import { useEffect, useState } from "react";
import { Area, AreaChart, CartesianGrid, XAxis } from "recharts";
import hospitalInfoData from "@/types/hospitalInfoData";
import getHospitalInfo from "@/services/fetching";



const chartConfig = {
  visitors: {
    label: "Visitors",
  },
  capacity: {
    label: "Capacity",
    color: "var(--chart-1)",
  },
  occupancy: {
    label: "Occupancy",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig


const chartData = [
    {date: "2025-08-13", capacity: 500, occupancy: 300},
    {date: "2025-08-14", capacity: 500, occupancy: 450},
    {date: "2025-08-15", capacity: 500, occupancy: 400},
    {date: "2025-08-16", capacity: 500, occupancy: 250},
    {date: "2025-08-17", capacity: 500, occupancy: 300},

]

const Offical = () => {
    const [hospitalInfo, setHospitalInfo] = useState<hospitalInfoData[]>([])

    useEffect(() => {

        if(hospitalInfo.length == 0) {
            getHospitalInfo({hospitalInfo :hospitalInfo, setHospitalInfo :setHospitalInfo, targetHospital: HOSPITALS.BURWOOD})

        }
        
        console.log(hospitalInfo)

    })

    return (
        <article className="w-[100%] flex">
            <section className="w-[50%]">
                <Card>
                    <CardHeader>
                        <CardTitle className="text-left">Hospitals</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {
                            hospitalInfo.map((key) => {
                                return (
                                    <HospitalInfo totalBeds={key.total_beds} intransit={key.in_transit} occupied={key.occupied} hospitalName={key.name} distance={Math.round(Math.random()*100)} has_burn_unit={key.has_burn_unit} has_icu={key.has_icu} has_water_unit={key.has_water_unit} />
                                )
                            })
                        }                    
                    </CardContent>
                </Card>

            </section>
            <section className="w-[50%]">
                <Tabs defaultValue="transfers">
                    <TabsList>
                        <TabsTrigger value="transfers">Transfers</TabsTrigger>
                        <TabsTrigger value="state">State</TabsTrigger>
                        <TabsTrigger value="predictions">Predictions</TabsTrigger>
                    </TabsList>
                    <TabsContent value="transfers">
                        <Card>
                            <CardHeader>
                                <CardTitle className="text-left">Transfers</CardTitle>
                            </CardHeader>
                            <CardContent>
                                <TransferButton />
                                
                            </CardContent>
                        </Card>
                    </TabsContent>
                    <TabsContent value="state">
                        <Card>
                            <CardHeader>
                                <CardTitle>Current State of the System</CardTitle>
                            </CardHeader>
                            <CardContent>
                                <ChartContainer
                                config={chartConfig}>
                                    <AreaChart data={chartData}>
                                        <defs>
                                            <linearGradient id="fillOcupancy" x1="0" y1="0" x2="0" y2="1">
                                                <stop
                                                offset="5%"
                                                stopColor="var(--destructive)"
                                                stopOpacity={0.8}
                                                />
                                                <stop
                                                offset="95%"
                                                stopColor="var(--destructive)"
                                                stopOpacity={0.1}
                                                />
                                            </linearGradient>
                                            <linearGradient id="fillCapacity" x1="0" y1="0" x2="0" y2="1">
                                                <stop
                                                offset="5%"
                                                stopColor="var(--chart-2)"
                                                stopOpacity={0.8}
                                                />
                                                <stop
                                                offset="95%"
                                                stopColor="var(--chart-2)"
                                                stopOpacity={0.1}
                                                />
                                            </linearGradient>
                                        </defs>
                                        <CartesianGrid vertical={false} />
                                        <XAxis
                                        dataKey="date"
                                        tickLine={false}
                                        axisLine={false}
                                        tickMargin={8}
                                        minTickGap={32}
                                        tickFormatter={(value) => {
                                            const date = new Date(value)
                                            return date.toLocaleDateString("en-US", {
                                            month: "short",
                                            day: "numeric",
                                            })
                                        }}
                                        />
                                        <ChartTooltip
                                        cursor={false}
                                        content={
                                            <ChartTooltipContent
                                            labelFormatter={(value) => {
                                                return new Date(value).toLocaleDateString("en-US", {
                                                month: "short",
                                                day: "numeric",
                                                })
                                            }}
                                            indicator="dot"
                                            />
                                        }
                                        />
                                        <Area
                                        dataKey="capacity"
                                        type="natural"
                                        fill="url(#fillCapacity)"
                                        stroke="var(--chart-2)"
                                        stackId="b" />
                                        <Area
                                        dataKey="occupancy"
                                        type="natural"
                                        fill="url(#fillOcupancy)"
                                        stroke="var(--destructive)"
                                        stackId="a"/>
                                    </AreaChart>
                                </ChartContainer>
                            </CardContent>
                        </Card>
                    </TabsContent>
                    <TabsContent value="predictions">
                        <p>This has not been implemented yet. This would be done using a model an an extenral server</p>

                    </TabsContent>
                </Tabs>
            </section>

        </article>
    )
}

export default Offical;