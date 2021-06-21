from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "tst_harvester tst_timelord_launcher tst_timelord tst_farmer tst_full_node tst_wallet".split(),
    "node": "tst_full_node".split(),
    "harvester": "tst_harvester".split(),
    "farmer": "tst_harvester tst_farmer tst_full_node tst_wallet".split(),
    "farmer-no-wallet": "tst_harvester tst_farmer tst_full_node".split(),
    "farmer-only": "tst_farmer".split(),
    "timelord": "tst_timelord_launcher tst_timelord tst_full_node".split(),
    "timelord-only": "tst_timelord".split(),
    "timelord-launcher-only": "tst_timelord_launcher".split(),
    "wallet": "tst_wallet tst_full_node".split(),
    "wallet-only": "tst_wallet".split(),
    "introducer": "tst_introducer".split(),
    "simulator": "tst_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
