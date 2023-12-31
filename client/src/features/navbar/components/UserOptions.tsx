import { Listbox, ListboxItem } from "@nextui-org/react";
import { useNavigate } from "react-router-dom";

import { AiFillHeart } from "react-icons/ai";
import { HiPencilSquare } from "react-icons/hi2";
import { BiBookAdd } from "react-icons/bi";
import { BsCardList, BsFillSunFill, BsMoonStarsFill } from "react-icons/bs";
import { RiAccountCircleFill } from "react-icons/ri";

import { IconWrapper } from "../../../components/IconWrapper"; 
import { useTheme } from "../../../hooks/useTheme";

export const UserOptions = () => {

  const navigate = useNavigate()

  const { mode, handleToggle } = useTheme()

  const handleClick = (key: string) => {

    if ( key === 'change-theme' ) return handleToggle()

    navigate(key)
  }

  return (
    <Listbox
      aria-label="User Menu"
      onAction={handleClick}
      className="p-0 gap-0 min-w-unit-8 divide-y divide-default-300/50 dark:divide-default-100/80 bg-content1 overflow-visible shadow-small rounded-medium"
      itemClasses={{
        base: "px-3 first:rounded-t-medium last:rounded-b-medium rounded-none gap-3 h-12 data-[hover=true]:bg-default-100/80",
      }}
    >
      <ListboxItem
        key="user/new-post"
        className="text-end"
        endContent={
          <IconWrapper className="bg-success/10 text-success">
            <BiBookAdd className="text-lg" />
          </IconWrapper>
        }
      >
        Crear Post
      </ListboxItem>
      <ListboxItem
        key="user/my-posts"
        className="text-end"
        endContent={
          <IconWrapper className="bg-secondary/10 text-secondary">
            <BsCardList className="text-lg" />
          </IconWrapper>
        }
      >
        Mis Posts
      </ListboxItem>
      <ListboxItem
        key="user/favourites"
        className="text-end"
        endContent={
          <IconWrapper className="bg-danger/10 text-danger">
            <AiFillHeart className="text-lg" />
          </IconWrapper>
        }
      >
        Favoritos
      </ListboxItem>
      <ListboxItem
        key="user/edit-profile"
        className="text-end"
        endContent={
          <IconWrapper className="bg-primary/10 text-primary">
            <HiPencilSquare className="text-lg" />
          </IconWrapper>
        }
      >
        Editar Perfil
      </ListboxItem>
      <ListboxItem
        key="change-theme"
        className="text-end"
        endContent={
          <IconWrapper className="bg-default-400/10 text-primary">
            {
              mode === 'light'
                ? <BsFillSunFill color="#fbbf24"/>
                : <BsMoonStarsFill color={'#b5afaa'} /> 
            }
          </IconWrapper>
        }
      >
        {
          mode === 'light' ? 'Modo Claro' : 'Modo Oscuro'
        }
      </ListboxItem>
      <ListboxItem
        key="user/logout"
        className="text-end"
        endContent={
          <IconWrapper className="bg-warning/10 text-warning">
            <RiAccountCircleFill className="text-lg" />
          </IconWrapper>
        }
      >
        Cerrar Sesion
      </ListboxItem>
    </Listbox>
  );
}
