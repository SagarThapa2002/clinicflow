from clinicflow.main import main


def test_main_runs(capsys):
    main()
    assert "ClinicFlow" in capsys.readouterr().out