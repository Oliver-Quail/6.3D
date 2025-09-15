import HOSPITALS from "@/misc/url";
import hospitalInfoData from "@/types/hospitalInfoData";

interface hospitalInfoProps {
    //hospitalInfo: Record<string, hospitalInfoData>
    targetHospital :HOSPITALS;


}

const getHospitalInfo = (props :hospitalInfoProps) => {

    let config :RequestInit = {
        method: "GET",
        mode: "cors"
    }



    let hospitalInfoPromise = fetch(props.targetHospital + "/api/hospital", config).then((hospitalDataRaw :Response) => {
        console.log(hospitalInfoPromise)
        hospitalDataRaw.json().then((hospitalInfo) => {
            console.log(hospitalInfo)
        }) 
    })
}


export default getHospitalInfo;        