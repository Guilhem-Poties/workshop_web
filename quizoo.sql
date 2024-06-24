-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 24 juin 2024 à 16:56
-- Version du serveur : 5.7.40
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `quizoo`
--

-- --------------------------------------------------------

--
-- Structure de la table `question`
--

DROP TABLE IF EXISTS `question`;
CREATE TABLE IF NOT EXISTS `question` (
  `id_question` int(8) NOT NULL,
  `libelle` varchar(50) NOT NULL,
  `id_theme` int(4) NOT NULL,
  `id_bonne_reponse` int(10) NOT NULL,
  PRIMARY KEY (`id_question`),
  KEY `id_theme` (`id_theme`),
  KEY `id_bonne_reponse` (`id_bonne_reponse`)
) ENGINE=MyISAM DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Structure de la table `reponse`
--

DROP TABLE IF EXISTS `reponse`;
CREATE TABLE IF NOT EXISTS `reponse` (
  `id_reponse` int(10) NOT NULL,
  `libelle` varchar(50) NOT NULL,
  `id_question` int(8) NOT NULL,
  PRIMARY KEY (`id_reponse`),
  KEY `id_question` (`id_question`)
) ENGINE=MyISAM DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Structure de la table `session`
--

DROP TABLE IF EXISTS `session`;
CREATE TABLE IF NOT EXISTS `session` (
  `id_session` int(8) NOT NULL,
  `date` text NOT NULL,
  `score` int(3) NOT NULL,
  `id_utilisateur` int(4) NOT NULL,
  `id_theme` int(4) NOT NULL,
  PRIMARY KEY (`id_session`),
  UNIQUE KEY `id_user` (`id_utilisateur`),
  KEY `id_theme` (`id_theme`)
) ENGINE=MyISAM DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Structure de la table `theme`
--

DROP TABLE IF EXISTS `theme`;
CREATE TABLE IF NOT EXISTS `theme` (
  `id_session` int(4) NOT NULL,
  `libelle` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`id_session`)
) ENGINE=MyISAM DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id_utilisateur` int(4) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `date_naissance` date NOT NULL,
  PRIMARY KEY (`id_utilisateur`)
) ENGINE=MyISAM DEFAULT CHARSET=utf16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
