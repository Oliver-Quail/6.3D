import HOSPITALS from "@/misc/url";
import hospitalInfoData from "@/types/hospitalInfoData";

interface hospitalInfoProps {
    hospitalInfo: Record<string, hospitalInfoData>;
    setHospitalInfo: (value: Record<string, hospitalInfoData>) => void;
    targetHospital :HOSPITALS;
}

const getHospitalInfo = (props :hospitalInfoProps) => {

    let config :RequestInit = {
        method: "GET",
        mode: "cors"
    }



    let hospitalInfoPromise = fetch(props.targetHospital + "/api/hospital", config).then((hospitalDataRaw :Response) => {
        hospitalDataRaw.json().then((hospitalInfo) => {
            let hosInfo = hospitalInfo[0] as hospitalInfoData;
            let copy = props.hospitalInfo;
            copy[hosInfo.name] = hosInfo
            props.setHospitalInfo(copy)

        }) 
    })
}


export default getHospitalInfo;        